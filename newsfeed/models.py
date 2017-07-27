from django.db import models
from cms.models import CMSPlugin

# Create your models here.
class Newspiece(models.Model):
    id = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=64)
    content = models.TextField(default='')

class NewspiecePluginModel(CMSPlugin):
    newspiece = models.ForeignKey(Newspiece)

    def __unicode__(self):
        return self.newspiece.headline
