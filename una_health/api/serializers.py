from rest_framework import serializers

from .models import Customer, Device, GlucoseData


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["user_id"]


class GlucoseDataSerializer(serializers.ModelSerializer):
    user = CustomerSerializer()
    device = DeviceSerializer()

    class Meta:
        model = GlucoseData
        fields = [
            "id",
            "user",
            "device",
            "device_timestamp",
            "record_type",
            "glucose_history",
            "glucose_scan",
            "non_numeric_rapid_acting_insulin",
            "rapid_acting_insulin",
            "non_numeric_food_data",
            "carbohydrates_grams",
            "carbohydrates_portions",
            "non_numeric_depot_insulin",
            "depot_insulin",
            "notes",
            "glucose_test_strips",
            "ketone",
            "meal_insulin",
            "corrective_insulin",
            "insulin_change_by_user",
        ]


class GlucoseDataUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

class GlucoseMinMaxSerializer(serializers.Serializer):
    min_value = serializers.IntegerField()
    max_value = serializers.IntegerField()