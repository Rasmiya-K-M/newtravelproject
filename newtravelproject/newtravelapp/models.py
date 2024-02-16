from django.db import models

# Create your models here.
#class name is the table name

class NewsandArticles(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to="pics")
    desc=models.TextField()

    def __str__(self):
        return self.name

class explore(models.Model):
    dest=models.CharField(max_length=250)
    image2=models.ImageField(upload_to="pics")
    about=models.TextField()

    def __str__(self):
        return self.dest