from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import pre_delete, post_save
from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import User
import csv
import json
import os
from django.utils import timezone

class UserProfile(models.Model):
    AVAILABLE_COLOURS = (
        ('BLK', 'black'),
        ('BLU', 'blue'),
        ('GRY', 'grey'),
        ('RED', 'red'),
        ('GRN', 'green'),
    )
    user = models.OneToOneField(User)
    sidebar_colour = models.CharField(max_length = 3, choices = AVAILABLE_COLOURS, default = 'BLK')
    admin_data_only = models.BooleanField(default = False)

@receiver(post_save, sender=User)
def creare_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user = instance)


class ChargingStation(models.Model):
    lat = models.DecimalField(max_digits=20, decimal_places=15)
    lon = models.DecimalField(max_digits=20, decimal_places=15)
    operator = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    admin = models.BooleanField(default=False)
    next_available = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return str(self.id)

    def inUse(self): 
        return self.next_available >= timezone.now()

class Upload(models.Model):
    def validate_file_extension(value):
        if not value.name.endswith('.csv'):
            raise ValidationError('Did not upload a csv file!')

    def validate_file_size(value):
        file_size = value.file.size
        size_limit = 10.0
        if file_size > size_limit*1024*1024:
            raise ValidationError("Max file size is %sMB" % str(size_limit))

    docfile = models.FileField(upload_to='documents/', validators=[validate_file_extension, validate_file_size])

    def parse(self):
        upload_path = os.path.abspath('media/' + self.docfile.name).replace("\\", "/")
        json_object = []
        with open(upload_path) as csv_file:
            for row in csv.DictReader(csv_file):
                json_object.append({
                    "LATITUDE": row['LATITUDE'],
                    "LONGITUDE": row['LONGITUDE'],
                    "LOT_OPERATOR": row['LOT_OPERATOR'],
                    "ADDRESS": row['ADDRESS']
                })
        output_json = json.dumps(json_object)
        return output_json

    def import_parsed(self, json_object):
        for object in json.loads(json_object):
            ChargingStation.objects.get_or_create(
                lat=object['LATITUDE'],
                lon=object['LONGITUDE'],
                operator=object['LOT_OPERATOR'],
                address=object['ADDRESS'],
                admin=True,
                )


# handles deleting media file for upload deletes
@receiver(pre_delete, sender=Upload)
def upload_delete(sender, instance, **kwargs):
    instance.docfile.delete(False)