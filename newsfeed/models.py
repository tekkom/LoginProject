from django.db import models

# Create your models here.
class Newspiece(models.Model):
    id = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=64)
    content = models.TextField(default='')
