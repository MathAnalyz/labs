from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=200)
    info = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class Division(models.Model):
    name = models.CharField(max_length=100)
    annotation = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Plant(models.Model):
    id = models.AutoField(primary_key=True)
    rus_name = models.CharField(max_length=500)
    lat_name = models.CharField(max_length=500)
    info = models.CharField(max_length=3000)
    sec_measures = models.CharField(max_length=2000)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    division = models.ForeignKey(Division, on_delete=models.PROTECT)
    reservations = models.ManyToManyField(Reservation)

    def __str__(self):
        return self.rus_name
