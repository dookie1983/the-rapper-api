from django.db import models

# Create your models here.
# - aka
# - name
# - age

class Artist(models.Model):
    aka = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    age = models.IntegerField()

class Meta:
    db_table = 'artist'