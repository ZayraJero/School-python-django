from django.db import models

# Create your models here.


class Bootcamp(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Koder(models.Model):

    full_name = models.CharField(max_length=500)
    email = models.EmailField(unique=True)

    bootcamp = models.ForeignKey(
        Bootcamp, related_name="koders", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.full_name