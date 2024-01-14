from django.db import models
from django.utils import timezone


# Create your models here.
class Bits(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'code= #{self.code} - time= #{self.timestamp}'


class Content(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=2000)
    bits = models.ForeignKey(Bits, on_delete=models.CASCADE, related_name='content')
    timestamp = models.DateTimeField(default=timezone.now)
    marked = models.BooleanField(default=False)

    def __str__(self):
        return f'content= #{self.content} - time= #{self.timestamp} - bits= #{self.bits}'

