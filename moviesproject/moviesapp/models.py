from django.db import models

# Create your models here.
class Movies(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField(null=True)
    year=models.IntegerField()
    img=models.ImageField(upload_to='image')

    def __str__(self):
        return self.name