from django.db import models
from datetime import datetime
#from schedule.models import Event, EventRelation, Calendar
from django.db.migrations.serializer import BaseSerializer
from django.db.migrations.writer import MigrationWriter

# Create your models here.
#ALTER SEQUENCE users_id_seq RESTART WITH 1

"""
class CalendarSerializer(BaseSerializer):
    def serialize(self):
        return repr(self.value), {'from schedule.models import Calendar'}
MigrationWriter.register_serializer(Calendar, CalendarSerializer)

def_cal = Calendar(name='Defaut Availibility',slug = 'Defaut Availibility'+)
def_cal.save()
"""
class Guide(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active =  models.BooleanField(default=True)
    time_start = models.DateTimeField(default="2000-1-1 1:00")
    time_end = models.DateTimeField(default="2000-1-1 1:00")

    """    
    availibility = models.ForeignKey(
    'schedule.Calendar', 
    on_delete=models.CASCADE,
    default=def_cal,
    )
    """
    def __str__(self):
        return self.first_name + " " + self.last_name

    def isAvailible(self, start_to_check, end_to_check):
        if start_to_check >= self.time_start and end_to_check < self.time_end:
            return True
        else:
            return False


class Destination(models.Model): #the stuff in the () tells django to convert this into a model 

    #id part not necessary, primary key is automatically created in databases
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics') #upload_to = the folder that will store all images of this manner
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    start_time = models.DateTimeField(default="2000-1-1 1:00")
    end_time = models.DateTimeField(default="2000-1-1 1:00")
    guides = models.ManyToManyField(Guide)

    def __str__(self):
        return self.name
    