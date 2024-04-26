from django.db import models

# Create your models here.


class Customer(models.Model):
    user_id = models.CharField(primary_key=True, max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.user_id


class Device(models.Model):
    device_name = models.CharField(max_length=255)
    serial_number = models.CharField(primary_key=True, max_length=255)

    def __str__(self) -> str:
        return self.serial_number


class GlucoseData(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.SET_NULL, null=True)
    device_timestamp = models.DateTimeField()
    record_type = models.IntegerField()
    glucose_history = models.IntegerField(null=True, blank=True)
    glucose_scan = models.IntegerField(null=True, blank=True)
    non_numeric_rapid_acting_insulin = models.CharField(
        max_length=255, null=True, blank=True
    )
    rapid_acting_insulin = models.IntegerField(null=True, blank=True)
    non_numeric_food_data = models.CharField(max_length=255, null=True, blank=True)
    carbohydrates_grams = models.IntegerField(null=True, blank=True)
    carbohydrates_portions = models.IntegerField(null=True, blank=True)
    non_numeric_depot_insulin = models.CharField(max_length=255, null=True, blank=True)
    depot_insulin = models.IntegerField(null=True, blank=True)
    notes = models.CharField(max_length=255, null=True, blank=True)
    glucose_test_strips = models.IntegerField(null=True, blank=True)
    ketone = models.IntegerField(null=True, blank=True)
    meal_insulin = models.IntegerField(null=True, blank=True)
    corrective_insulin = models.IntegerField(null=True, blank=True)
    insulin_change_by_user = models.IntegerField(null=True, blank=True)
