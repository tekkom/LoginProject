from django.db import models

# Create your models here.
class Group(models.Model):
    gName = models.CharField(max_length=100)

    def __str__(self):
        return self.gName

class User(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    uName = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.group + ' - ' + self.uName

