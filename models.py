from django.db import models
import uuid

class Entry_Exit(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    id =  models.IntegerField(blank=True, null=False,primary_key=True)
    age = models.IntegerField(blank=True, null=True)
    dob = models.DateField(("Date"),blank=True, null=True)
    gate_entry_number = models.IntegerField(blank=True, null=True)
    entry_timestamp = models.DateTimeField(blank=True, null=True)
    exit_timestamp = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
       verbose_name = "Entry Exit"
       verbose_name_plural = "Entry Exit"
