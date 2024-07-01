from django.conf import settings
from django.test import TestCase
from django.core.management import call_command
from .models import Log
from io import StringIO
from django.core.management.base import CommandError
from log.apps import LogConfig

# Create your tests here.
class LogSerializerTestCase(TestCase):
    def testSimple(self):
        line = Log.objects.create(ip = "127.0.0.1", URI = "http://localhost", userAgent = "Firefox")        
        self.assertEqual(str(line), "127.0.0.1")

    # Проверка managment command
    def testCommand(self):
        out = StringIO()
        call_command("log", "files/test.txt", stdout=out)
        self.assertEqual(out.getvalue(), "OK\n")

    # Изменяем maxFileSize чтобы смоделировать превышение размера файла
    def testCommandBigFile(self):
        with self.assertRaises(CommandError):
            LogConfig.maxFileSize = 1024           
            call_command("log", "files/test2.txt")