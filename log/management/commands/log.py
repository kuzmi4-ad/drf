from django.apps import AppConfig
from django.core.management.base import BaseCommand, CommandError
from log.apps import LogConfig
from log.models import Log
import json, os
import hashlib
from datetime import datetime

class Command(BaseCommand):
    help = 'pyton manage.py $filename'
    
    def add_arguments(self, parser):
        # Добавляем аргумент для указания пути к файлу логов
        parser.add_argument('logfile', type=str, help='Path to the log file')
    
    def handle(self, *args, **options):
        logfile_path = options['logfile']
        
        try:
            with open(logfile_path, 'r') as logfile:
                # Ограничение на размер файла             
                if(os.path.getsize(logfile_path) > LogConfig.maxFileSize): 
                    raise CommandError(f'File size should not exceed {LogConfig.maxFileSize} bytes!')                
                for line in logfile:
                    row = json.loads(line)                    
                    request = row['request'].split()
                    b = Log()
                    b.ip = row['remote_ip']
                    b.date = datetime.strptime(row['time'], "%d/%b/%Y:%H:%M:%S %z")
                    b.httpMethod = request[0]
                    b.URI = request[1]
                    b.responceCode = row['response']
                    b.responceSize = row['bytes']
                    b.userAgent = row['agent']
                    b.user = row['remote_user']
                    # Уникальный primary_key, чтобы не дублировать записи
                    b.hash = hashlib.md5(line.encode()).hexdigest()
                    b.save()                       
        except FileNotFoundError:
            raise CommandError(f'The file "{logfile_path}" does not exist.')
        return "OK"