from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    desc = models.TextField()

    def __str__(self):
        return self.name + " " + self.desc

class Books(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField()
    url = models.URLField()
    desc = models.TextField()

    def __str__(self):
        return self.title + " " + self.desc

class Sign(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=60)
    # password2 = models.CharField(max_length=15)
    def __str__(self):
        return self.username
