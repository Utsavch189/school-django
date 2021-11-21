from django.db import models
from django.db.models.fields import DateField
# Create your models here.
class notic(models.Model):
    title=models.CharField(max_length=100)
    pdf=models.FileField()

class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.desc + ' by ' + self.name



class class5(models.Model):
    title=models.CharField(max_length=100)
    pdf=models.FileField()
    date=models.DateField()

class class6(models.Model):
    title=models.CharField(max_length=100)
    pdf=models.FileField()
    date=models.DateField()

class class7(models.Model):
    title=models.CharField(max_length=100)
    pdf=models.FileField()
    date=models.DateField()

class class8(models.Model):
    title=models.CharField(max_length=100)
    pdf=models.FileField()
    date=models.DateField()


class class9(models.Model):
    title=models.CharField(max_length=100)
    pdf=models.FileField()
    date=models.DateField()



class class10(models.Model):
    title=models.CharField(max_length=100)
    pdf=models.FileField()
    date=models.DateField()