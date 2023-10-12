from django.db import models

# Create your models here.


class Brunch(models.Model):
    nombre = models.CharField(max_length=30)
    zona = models.CharField(max_length=30)
    desc = models.CharField(max_length=50)
    puntaje = models.IntegerField()
    tarjcred = models.BooleanField()


class Almuerzo(models.Model):
    nombre = models.CharField(max_length=30)
    zona = models.CharField(max_length=30)
    desc = models.CharField(max_length=50)
    puntaje = models.IntegerField()
    tarjcred = models.BooleanField()


class Merienda(models.Model):
    nombre = models.CharField(max_length=30)
    zona = models.CharField(max_length=30)
    desc = models.CharField(max_length=50)
    puntaje = models.IntegerField()
    tarjcred = models.BooleanField()


class Cena(models.Model):
    nombre = models.CharField(max_length=30)
    zona = models.CharField(max_length=30)
    desc = models.CharField(max_length=50)
    puntaje = models.IntegerField()
    tarjcred = models.BooleanField()
