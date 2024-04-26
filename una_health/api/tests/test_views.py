from datetime import datetime
from io import StringIO

from api.models import Customer, Device, GlucoseData
from api.serializers import GlucoseDataSerializer
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.utils import timezone


def test_data_create():
    user1 = Customer.objects.create(user_id="user1")
    user2 = Customer.objects.create(user_id="user2")

    device1 = Device.objects.create(
        device_name="FreeStyle",
        serial_number="ABC-123-XYZ-456-8",
    )

    device2 = Device.objects.create(
        device_name="FreeStyle",
        serial_number="ABC-123-XYZ-456-9",
    )

    for i in range(4):
        GlucoseData.objects.create(
            user=user1,
            device=device1,
            device_timestamp=datetime(
                year=2024, month=4, day=26, hour=12, minute=30, second=i
            ),
            record_type=5 + i,
            glucose_history=185 + i,
            glucose_scan=201 + i,
            non_numeric_rapid_acting_insulin="abc",
            rapid_acting_insulin=12 + i,
            non_numeric_food_data="apple",
            carbohydrates_grams=100 + i,
            carbohydrates_portions=5 + i,
            non_numeric_depot_insulin="xyz",
            depot_insulin=15 + i,
            notes="in testing phase",
            glucose_test_strips=2 + i,
            ketone=10 + i,
            meal_insulin=20 + i,
            corrective_insulin=50 + i,
            insulin_change_by_user=5 + i,
        )

    for i in range(10, 15):
        GlucoseData.objects.create(
            user=user2,
            device=device2,
            device_timestamp=datetime(
                year=2025, month=4, day=26, hour=12, minute=30, second=i
            ),
            record_type=5 + i,
            glucose_history=185 + i,
            glucose_scan=201 + i,
            non_numeric_rapid_acting_insulin="abc",
            rapid_acting_insulin=12 + i,
            non_numeric_food_data="apple",
            carbohydrates_grams=100 + i,
            carbohydrates_portions=5 + i,
            non_numeric_depot_insulin="xyz",
            depot_insulin=15 + i,
            notes="in testing phase",
            glucose_test_strips=2 + i,
            ketone=10 + i,
            meal_insulin=20 + i,
            corrective_insulin=50 + i,
            insulin_change_by_user=5 + i,
        )


class GlucoseDataListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_data_create()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/api/v1/levels/")
        self.assertEqual(response.status_code, 200)

    def test_filter_by_user_id(self):
        response = self.client.get("/api/v1/levels/?user_id=user2")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data[3]["user"]["user_id"], "user2")

    def test_filter_by_user_id(self):
        response = self.client.get("/api/v1/levels/?user_id=user2")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data[3]["user"]["user_id"], "user2")

    def test_filter_by_timestamp_range(self):
        start_timestamp = datetime(
            year=2025, month=4, day=26, hour=12, minute=30, second=10
        )
        stop_timestamp = datetime(
            year=2025, month=4, day=26, hour=12, minute=30, second=13
        )
        response = self.client.get(
            f"/api/v1/levels/?start_timestamp={start_timestamp}&stop_timestamp={stop_timestamp}"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data[3]["user"]["user_id"], "user2")

    def test_no_filter(self):
        response = self.client.get("/api/v1/levels/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 9)


class GlucoseDataSingleViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_data_create()

    def test_retrieve_single_glucose_data(self):
        response = self.client.get("/api/v1/levels/3/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["user"]["user_id"], "user1")
        self.assertEqual(response.data["device_timestamp"], "2024-04-26T12:30:02Z")


class PrepopulateGlucoseDataTest(TestCase):
    def test_post_method(self):
        csv_data = (
            "Glukose-Werte,Erstellt am,25-02-2021 09:55 UTC,Erstellt von,ccc\n"
            "\n"
            "Gerät,Seriennummer,Gerätezeitstempel,Aufzeichnungstyp,Glukosewert-Verlauf mg/dL,Glukose-Scan mg/dL,"
            "Nicht numerisches schnellwirkendes Insulin,Schnellwirkendes Insulin (Einheiten),Nicht numerische Nahrungsdaten,"
            "Kohlenhydrate (Gramm),Kohlenhydrate (Portionen),Nicht numerisches Depotinsulin,Depotinsulin (Einheiten),"
            "Notizen,Glukose-Teststreifen mg/dL,Keton mmol/L,Mahlzeiteninsulin (Einheiten),Korrekturinsulin (Einheiten),"
            "Insulin-Änderung durch Anwender (Einheiten)\n"
            "FreeStyle LibreLink,e09bb0f0-018b-429b-94c7-62bb306a0136,10-02-2021 09:40,0,139,,,,,,,,,,,,,,\n"
            "FreeStyle LibreLink,e09bb0f0-018b-429b-94c7-62bb306a0136,10-02-2021 09:55,0,138,,,,,,,,,,,,,,\n"
            "FreeStyle LibreLink,e09bb0f0-018b-429b-94c7-62bb306a0136,10-02-2021 10:10,0,140,,,,,,,,,,,,,,\n"
            "FreeStyle LibreLink,e09bb0f0-018b-429b-94c7-62bb306a0136,10-02-2021 10:25,0,149,,,,,,,,,,,,,,\n"
            "FreeStyle LibreLink,e09bb0f0-018b-429b-94c7-62bb306a0136,10-02-2021 10:40,0,155,,,,,,,,,,,,,,\n"
            "FreeStyle LibreLink,e09bb0f0-018b-429b-94c7-62bb306a0136,10-02-2021 10:55,0,153,,,,,,,,,,,,,,\n"
            "FreeStyle LibreLink,e09bb0f0-018b-429b-94c7-62bb306a0136,10-02-2021 11:10,0,151,,,,,,,,,,,,,,\n"
            "FreeStyle LibreLink,e09bb0f0-018b-429b-94c7-62bb306a0136,10-02-2021 11:25,0,148,33,55,66,66,66,66,55,66,77,33,66,22,66,\n"
            "FreeStyle LibreLink,e09bb0f0-018b-429b-94c7-62bb306a0136,10-02-2021 11:40,0,144,,,,100,,,,,,,,,,\n"
            "FreeStyle LibreLink,e09bb0f0-018b-429b-94c7-62bb306a0136,10-02-2021 11:55,0,145,,,,,,,,,,,,,,\n"
            "FreeStyle LibreLink,e09bb0f0-018b-429b-94c7-62bb306a0136,10-02-2021 12:10,0,143,,,,,,,,,,,,,,\n"
            "FreeStyle LibreLink,e09bb0f0-018b-429b-94c7-62bb306a0136,10-02-2021 12:25,0,139,,,,,,,,,,,,,,\n"
            "FreeStyle LibreLink,e09bb0f0-018b-429b-94c7-62bb306a0136,10-02-2021 12:40,0,136,,,,,,,,,,,,,,\n"
            "FreeStyle LibreLink,e09bb0f0-018b-429b-94c7-62bb306a0136,10-02-2021 12:55,0,132,,,,,,,,,,,,,,\n"
        )

        csv_file = StringIO(csv_data)

        file_name = "user1.csv"
        csv_file_upload = SimpleUploadedFile(
            file_name, csv_data.encode("utf-8"), content_type="text/csv"
        )
        response = self.client.post(
            "/api/v1/prepopulate-data/", {"file": csv_file_upload}, format="multipart"
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(GlucoseData.objects.exists())

        # response = self.client.get("/api/v1/levels/")
        # self.assertEqual(len(response.data), 14)
        # self.assertEqual(response.data[3]['user']['user_id'], 'user1')
