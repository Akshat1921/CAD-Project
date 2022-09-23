from django.db import models
 
def upload_path(instance, filname):
    return '/'.join(['covers', str(instance.title), filname])
 
class Book(models.Model):
    title = models.CharField(max_length=32, blank=False)
    cover = models.ImageField(blank=True, null=True, upload_to=upload_path)
 
class StockFile(models.Model):
    name = models.CharField(max_length=32,blank=False)
    price = models.IntegerField(null=False,blank=False)
    volume = models.IntegerField(null=False,blank=False)
    info = models.FileField(null=False,blank=False)