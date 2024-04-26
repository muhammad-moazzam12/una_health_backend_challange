from datetime import datetime

from api.models import Customer, Device, GlucoseData
from django.test import TestCase
from django.utils import timezone


class CustomerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(user_id="abc-123")

    def test_user_id_label(self):
        customer = Customer.objects.get(user_id="abc-123")
        field_label = customer._meta.get_field("user_id").verbose_name
        self.assertEqual(field_label, "user id")

    def test_is_active_label(self):
        customer = Customer.objects.get(user_id="abc-123")
        field_label = customer._meta.get_field("is_active").verbose_name
        self.assertEqual(field_label, "is active")

    def test_user_id_max_length(self):
        customer = Customer.objects.get(user_id="abc-123")
        max_length = customer._meta.get_field("user_id").max_length
        self.assertEqual(max_length, 255)

    def test_is_active_default_value(self):
        customer = Customer.objects.get(user_id="abc-123")
        is_active_default = True
        self.assertEqual(customer.is_active, is_active_default)

    def test_primary_key(self):
        customer = Customer.objects.get(user_id="abc-123")
        self.assertEqual(customer.pk, "abc-123")


class DeviceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Device.objects.create(
            device_name="FreeStyle LibreLink",
            serial_number="123-ABC-456-XYZ-1",
        )

    def test_device_label(self):
        device = Device.objects.get(serial_number="123-ABC-456-XYZ-1")
        field_label = device._meta.get_field("device_name").verbose_name
        self.assertEqual(field_label, "device name")

    def test_serial_number_label(self):
        device = Device.objects.get(serial_number="123-ABC-456-XYZ-1")
        field_label = device._meta.get_field("serial_number").verbose_name
        self.assertEqual(field_label, "serial number")

    def test_device_max_length(self):
        device = Device.objects.get(serial_number="123-ABC-456-XYZ-1")
        max_length = device._meta.get_field("device_name").max_length
        self.assertEqual(max_length, 255)

    def test_serial_number_max_length(self):
        device = Device.objects.get(serial_number="123-ABC-456-XYZ-1")
        max_length = device._meta.get_field("serial_number").max_length
        self.assertEqual(max_length, 255)

    def test_primary_key(self):
        device = Device.objects.get(serial_number="123-ABC-456-XYZ-1")
        self.assertEqual(device.pk, "123-ABC-456-XYZ-1")


class GlucoseDataTest(TestCase):
    @classmethod
    def setUp(cls):
        customer = Customer.objects.create(user_id="mike-123")
        device = Device.objects.create(
            device_name="FreeStyle123", serial_number="1D48A10E-4888-8158-026F08814832"
        )
        GlucoseData.objects.create(
            user=customer,
            device=device,
            device_timestamp=timezone.now(),
            record_type=5,
            glucose_history=185,
            glucose_scan=201,
            non_numeric_rapid_acting_insulin="abc",
            rapid_acting_insulin=12,
            non_numeric_food_data="apple",
            carbohydrates_grams=100,
            carbohydrates_portions=5,
            non_numeric_depot_insulin="xyz",
            depot_insulin=15,
            notes="in testing phase",
            glucose_test_strips=2,
            ketone=10,
            meal_insulin=20,
            corrective_insulin=50,
            insulin_change_by_user=5,
        )

    # test labels
    def test_user_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_device_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field("device").verbose_name
        self.assertEqual(field_label, "device")

    def test_device_timestamp_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field("device_timestamp").verbose_name
        self.assertEqual(field_label, "device timestamp")

    def test_record_type_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field("record_type").verbose_name
        self.assertEqual(field_label, "record type")

    def test_glucose_history_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field("glucose_history").verbose_name
        self.assertEqual(field_label, "glucose history")

    def test_glucose_scan_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field("glucose_scan").verbose_name
        self.assertEqual(field_label, "glucose scan")

    def test_non_numeric_rapid_acting_insulin_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field(
            "non_numeric_rapid_acting_insulin"
        ).verbose_name
        self.assertEqual(field_label, "non numeric rapid acting insulin")

    def test_rapid_acting_insulin_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field("rapid_acting_insulin").verbose_name
        self.assertEqual(field_label, "rapid acting insulin")

    def test_non_numeric_food_data_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field("non_numeric_food_data").verbose_name
        self.assertEqual(field_label, "non numeric food data")

    def test_carbohydrates_grams_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field("carbohydrates_grams").verbose_name
        self.assertEqual(field_label, "carbohydrates grams")

    def test_carbohydrates_portions_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field(
            "carbohydrates_portions"
        ).verbose_name
        self.assertEqual(field_label, "carbohydrates portions")

    def test_non_numeric_depot_insulin_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field(
            "non_numeric_depot_insulin"
        ).verbose_name
        self.assertEqual(field_label, "non numeric depot insulin")

    def test_depot_insulin_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field("depot_insulin").verbose_name
        self.assertEqual(field_label, "depot insulin")

    def test_notes_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field("notes").verbose_name
        self.assertEqual(field_label, "notes")

    def test_glucose_test_strips_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field("glucose_test_strips").verbose_name
        self.assertEqual(field_label, "glucose test strips")

    def test_ketone_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field("ketone").verbose_name
        self.assertEqual(field_label, "ketone")

    def test_meal_insulin_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field("meal_insulin").verbose_name
        self.assertEqual(field_label, "meal insulin")

    def test_corrective_insulin_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field("corrective_insulin").verbose_name
        self.assertEqual(field_label, "corrective insulin")

    def test_insulin_change_by_user_label(self):
        glucose_data = GlucoseData.objects.get(id=1)
        field_label = glucose_data._meta.get_field(
            "insulin_change_by_user"
        ).verbose_name
        self.assertEqual(field_label, "insulin change by user")

    # test max-length
    def test_non_numeric_rapid_acting_insulin_max_length(self):
        glucose_data = GlucoseData.objects.get(id=1)
        max_length = glucose_data._meta.get_field(
            "non_numeric_rapid_acting_insulin"
        ).max_length
        self.assertEqual(max_length, 255)

    def test_non_numeric_food_data_max_length(self):
        glucose_data = GlucoseData.objects.get(id=1)
        max_length = glucose_data._meta.get_field("non_numeric_food_data").max_length
        self.assertEqual(max_length, 255)

    def test_non_numeric_depot_insulin_max_length(self):
        glucose_data = GlucoseData.objects.get(id=1)
        max_length = glucose_data._meta.get_field(
            "non_numeric_depot_insulin"
        ).max_length
        self.assertEqual(max_length, 255)

    def test_notes_max_length(self):
        glucose_data = GlucoseData.objects.get(id=1)
        max_length = glucose_data._meta.get_field("notes").max_length
        self.assertEqual(max_length, 255)

    # test  foreign key
    def test_customer_foreign_key(self):
        glucose_data = GlucoseData.objects.get(id=1)
        customer = glucose_data.user
        self.assertIsInstance(customer, Customer)

    def test_device_foreign_key(self):
        glucose_data = GlucoseData.objects.get(id=1)
        customer = glucose_data.device
        self.assertIsInstance(customer, Device)

    # test foreign key on delete
    def test_user_on_delete(self):
        customer = Customer.objects.get(user_id="mike-123")
        customer.delete()
        with self.assertRaises(GlucoseData.DoesNotExist):
            GlucoseData.objects.get(id=1)

    def test_device_on_delete(self):
        device = Device.objects.get(serial_number="1D48A10E-4888-8158-026F08814832")
        device.delete()
        glucose_data = GlucoseData.objects.get(id=1)
        self.assertIsNone(glucose_data.device)

    # test null
    def test_device_null(self):
        customer = GlucoseData.objects.get(id=1).user
        glucose_data = GlucoseData.objects.create(
            user=customer, device=None, device_timestamp=timezone.now(), record_type=5
        )

        self.assertIsNone(glucose_data.device)

    def test_glucose_history_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer,
            device=device,
            device_timestamp=timezone.now(),
            record_type=5,
            glucose_history=None,
        )

        self.assertIsNone(glucose_data.glucose_history)

    def test_glucose_scan_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer,
            device=device,
            device_timestamp=timezone.now(),
            record_type=5,
            glucose_scan=None,
        )

        self.assertIsNone(glucose_data.glucose_scan)

    def test_non_numeric_rapid_acting_insulin_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer,
            device=device,
            device_timestamp=timezone.now(),
            record_type=5,
            non_numeric_rapid_acting_insulin=None,
        )

        self.assertIsNone(glucose_data.non_numeric_rapid_acting_insulin)

    def test_rapid_acting_insulin_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer,
            device=device,
            device_timestamp=timezone.now(),
            record_type=5,
            rapid_acting_insulin=None,
        )

        self.assertIsNone(glucose_data.rapid_acting_insulin)

    def non_numeric_food_data(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer,
            device=device,
            device_timestamp=timezone.now(),
            record_type=5,
            non_numeric_food_data=None,
        )

        self.assertIsNone(glucose_data.non_numeric_food_data)

    def test_carbohydrates_grams_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer,
            device=device,
            device_timestamp=timezone.now(),
            record_type=5,
            carbohydrates_grams=None,
        )

        self.assertIsNone(glucose_data.carbohydrates_grams)

    def test_carbohydrates_portions_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer,
            device=device,
            device_timestamp=timezone.now(),
            record_type=5,
            carbohydrates_portions=None,
        )

        self.assertIsNone(glucose_data.carbohydrates_portions)

    def test_non_numeric_depot_insulin_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer,
            device=device,
            device_timestamp=timezone.now(),
            record_type=5,
            non_numeric_depot_insulin=None,
        )

        self.assertIsNone(glucose_data.non_numeric_depot_insulin)

    def test_depot_insulin_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer,
            device=device,
            device_timestamp=timezone.now(),
            record_type=5,
            depot_insulin=None,
        )

        self.assertIsNone(glucose_data.depot_insulin)

    def test_notes_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer,
            device=device,
            device_timestamp=timezone.now(),
            record_type=5,
            notes=None,
        )

        self.assertIsNone(glucose_data.notes)

    def test_glucose_test_strips_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer,
            device=device,
            device_timestamp=timezone.now(),
            record_type=5,
            glucose_test_strips=None,
        )

        self.assertIsNone(glucose_data.glucose_test_strips)

    def test_ketone_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer,
            device=device,
            device_timestamp=timezone.now(),
            record_type=5,
            ketone=None,
        )

        self.assertIsNone(glucose_data.ketone)

    def test_meal_insulin_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer,
            device=device,
            device_timestamp=timezone.now(),
            record_type=5,
            meal_insulin=None,
        )

        self.assertIsNone(glucose_data.meal_insulin)

    def test_corrective_insulin_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer,
            device=device,
            device_timestamp=timezone.now(),
            record_type=5,
            corrective_insulin=None,
        )

        self.assertIsNone(glucose_data.corrective_insulin)

    def test_insulin_change_by_user_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer,
            device=device,
            device_timestamp=timezone.now(),
            record_type=5,
            insulin_change_by_user=None,
        )

        self.assertIsNone(glucose_data.insulin_change_by_user)

    # test blank
    def test_device_null(self):
        customer = GlucoseData.objects.get(id=1).user
        glucose_data = GlucoseData.objects.create(
            user=customer, device_timestamp=timezone.now(), record_type=5
        )

        self.assertIsNone(glucose_data.device)

    def test_glucose_history_blank(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer, device=device, device_timestamp=timezone.now(), record_type=5
        )

        self.assertIsNone(glucose_data.glucose_history)

    def test_glucose_scan_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer, device=device, device_timestamp=timezone.now(), record_type=5
        )

        self.assertIsNone(glucose_data.glucose_scan)

    def test_non_numeric_rapid_acting_insulin_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer, device=device, device_timestamp=timezone.now(), record_type=5
        )

        self.assertIsNone(glucose_data.non_numeric_rapid_acting_insulin)

    def test_rapid_acting_insulin_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer, device=device, device_timestamp=timezone.now(), record_type=5
        )

        self.assertIsNone(glucose_data.rapid_acting_insulin)

    def non_numeric_food_data(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer, device=device, device_timestamp=timezone.now(), record_type=5
        )

        self.assertIsNone(glucose_data.non_numeric_food_data)

    def test_carbohydrates_grams_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer, device=device, device_timestamp=timezone.now(), record_type=5
        )

        self.assertIsNone(glucose_data.carbohydrates_grams)

    def test_carbohydrates_portions_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer, device=device, device_timestamp=timezone.now(), record_type=5
        )

        self.assertIsNone(glucose_data.carbohydrates_portions)

    def test_non_numeric_depot_insulin_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer, device=device, device_timestamp=timezone.now(), record_type=5
        )

        self.assertIsNone(glucose_data.non_numeric_depot_insulin)

    def test_depot_insulin_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer, device=device, device_timestamp=timezone.now(), record_type=5
        )

        self.assertIsNone(glucose_data.depot_insulin)

    def test_notes_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer, device=device, device_timestamp=timezone.now(), record_type=5
        )

        self.assertIsNone(glucose_data.notes)

    def test_glucose_test_strips_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer, device=device, device_timestamp=timezone.now(), record_type=5
        )

        self.assertIsNone(glucose_data.glucose_test_strips)

    def test_ketone_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer, device=device, device_timestamp=timezone.now(), record_type=5
        )

        self.assertIsNone(glucose_data.ketone)

    def test_meal_insulin_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer, device=device, device_timestamp=timezone.now(), record_type=5
        )

        self.assertIsNone(glucose_data.meal_insulin)

    def test_corrective_insulin_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer, device=device, device_timestamp=timezone.now(), record_type=5
        )

        self.assertIsNone(glucose_data.corrective_insulin)

    def test_insulin_change_by_user_null(self):
        customer = GlucoseData.objects.get(id=1).user
        device = GlucoseData.objects.get(id=1).device
        glucose_data = GlucoseData.objects.create(
            user=customer, device=device, device_timestamp=timezone.now(), record_type=5
        )

        self.assertIsNone(glucose_data.insulin_change_by_user)
