from django.db import models

# Create your models here.
class Log(models.Model):
    ip = models.CharField(max_length=100, default=None, blank=True, null=True)
    date = models.DateTimeField(default=None, blank=True, null=True)
    httpMethod = models.CharField(max_length=100, default=None, blank=True, null=True)
    URI = models.CharField(max_length=200, default=None, blank=True, null=True)
    responceCode = models.IntegerField(default=None, blank=True, null=True)
    responceSize = models.IntegerField(default=None, blank=True, null=True)
    userAgent = models.CharField(max_length=100, default=None, blank=True, null=True)
    user = models.CharField(max_length=100, default=None, blank=True, null=True)
    hash = models.CharField(max_length=200, default=0, primary_key=True)

    def __str__(self):
        return self.ip