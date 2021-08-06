from django.db import models
from django.conf import settings
# Create your models here.


class company_maker(models.Model):
        name = models.CharField(max_length=45)
        country = models.CharField(max_length=45)



class CD(models.Model):
    create_date = models.DateField()
    price = models.IntegerField(max_length=15)
    company_id = models.ForeignKey(company_maker, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)



class SellArrival(models.Model):
    op_date = models.DateField()
    op_code = models.CharField(max_length=1, choices=[
        ('S', 'Sell'),
        ('A', 'Arrival'),
    ])
    amount = models.IntegerField(max_length=15)
    supplier = models.CharField(max_length=15)
    price = models.IntegerField(max_length=15)
    CD_id = models.ForeignKey(CD, on_delete=models.CASCADE)


class Album(models.Model):
    genre = models.CharField(max_length=45)
    length = models.IntegerField(max_length=15)
    track_amount = models.IntegerField(max_length=15)
    out_date = models.DateField()
    album_name = models.CharField(max_length=45)


class Track(models.Model):
    track_name = models.CharField(max_length=17)
    author = models.CharField(max_length=25)
    performer = models.CharField(max_length=25)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)


class CdHasAlbum(models.Model):
    CD_id = models.ForeignKey(CD, on_delete=models.CASCADE)
    Album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
