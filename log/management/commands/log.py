from django.apps import AppConfig
from django.core.management.base import BaseCommand, CommandError
from log.apps import LogConfig
from log.models import Log
from log.gd import GD
import json
import os
import hashlib
from datetime import datetime
from django.core.exceptions import ValidationError


class Command(BaseCommand):
    help = 'python manage.py log https://drive.google.com/file/d/18Ss9afYL8xTeyVd0ZTfFX9dqja4pBGVp/view'

    

    def add_arguments(self, parser):
        # Добавляем аргумент для указания пути к файлу логов
        parser.add_argument('url', type=str, help='Url to the log file')

    def handle(self, *args, **options):
        logfile_path = "files/log.txt"
        url = options['url']
        file_id = url.split('/')[5]
        responce = GD.load(file_id)

        length = int(responce.headers.get("Content-length"))
        status = responce.status_code

        if (status != 200):
            raise CommandError(f'Error loading file, status {status}')

        if (length > LogConfig.maxFileSize):
            raise CommandError(
                f'File size should not exceed {LogConfig.maxFileSize} bytes!')

        GD.save(responce, logfile_path)

        try:
            with open(logfile_path, 'r') as logfile:
                list = []
                for index, line in enumerate(logfile):
                    row = json.loads(line)
                    request = row['request'].split()
                    b = Log()
                    b.ip = row['remote_ip']
                    b.date = datetime.strptime(
                        row['time'], "%d/%b/%Y:%H:%M:%S %z")
                    b.httpMethod = request[0]
                    b.URI = request[1]
                    b.responceCode = row['response']
                    b.responceSize = row['bytes']
                    b.userAgent = row['agent']
                    b.user = row['remote_user']
                    # Уникальный primary_key, чтобы не дублировать записи
                    b.hash = hashlib.md5(line.encode()).hexdigest()
                    try:
                        b.clean_fields()
                    except ValidationError as e:
                        print(f"Ошибка валидации, строка {index+1}: {e}")
                    else:
                        list.append(b)
                for i in range(0, len(list), 999):  # SQLite limit
                    Log.objects.bulk_create(list[i:i+999], ignore_conflicts=True)               
        except FileNotFoundError:
            raise CommandError(f'The file "{logfile_path}" does not exist.')
        return "OK"

            
