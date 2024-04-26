from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.CharField(primary_key=True)
    is_active = models.BooleanField(default=True)


class Device(models.Model):
    TYPE = ("FreeStyle LibreLink", "FreeStyle LibreLink")
    device = models.CharField(max_length=255, choices=TYPE)
    serial_number = models.CharField(max_length=255)


class GlucoseData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.SET_NULL)
    device_timestamp = models.DateTimeField()
    record_type = models.IntegerField()
    glucose_history = models.IntegerField(null=True, blank=True)
    glucose_scan = models.IntegerField(null=True, blank=True)
    non_numeric_rapid_acting_insulin = models.CharField(
        max_length=255, null=True, blank=True
    )
    rapid_acting_insulin = models.IntegerField(null=True, blank=True)
    non_numeric_food_data = models.CharField(max_length=255, null=True, blank=True)
    carbohydrates_grams = models.FloatField(null=True, blank=True)
    carbohydrates_portions = models.IntegerField(null=True, blank=True)
    non_numeric_depot_insulin = models.CharField(max_length=255, null=True, blank=True)
    depot_insulin = models.IntegerField(null=True, blank=True)
    notes = models.CharField(max_length=255, null=True, blank=True)
    glucose_test_strips = models.IntegerField(null=True, blank=True)
    ketone = models.IntegerField(null=True, blank=True)
    meal_insulin = models.IntegerField(null=True, blank=True)
    corrective_insulin = models.IntegerField(null=True, blank=True)
    insulin_change_by_user = models.IntegerField(null=True, blank=True)
