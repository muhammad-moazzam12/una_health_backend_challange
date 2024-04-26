import logging
from datetime import datetime
from io import StringIO

from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Customer, Device, GlucoseData
from .serializers import GlucoseDataSerializer, GlucoseDataUploadSerializer


class GlucoseDataListView(generics.ListAPIView):
    queryset = GlucoseData.objects.all()
    serializer_class = GlucoseDataSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ["device_timestamp"]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        # Get query parameters
        user_id = self.request.query_params.get("user_id")
        start_timestamp = self.request.query_params.get("start_timestamp")
        stop_timestamp = self.request.query_params.get("stop_timestamp")

        # Start with all GlucoseData objects
        queryset = GlucoseData.objects.all()

        # Apply filters if provided
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        if start_timestamp:
            queryset = queryset.filter(device_timestamp__gte=start_timestamp)
        if stop_timestamp:
            queryset = queryset.filter(device_timestamp__lte=stop_timestamp)

        return queryset

    # Swagger documentation for filtering parameters
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "user_id",
                openapi.IN_QUERY,
                description="Filter by user ID",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "start_timestamp",
                openapi.IN_QUERY,
                description="Filter by start timestamp",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "stop_timestamp",
                openapi.IN_QUERY,
                description="Filter by stop timestamp",
                type=openapi.TYPE_STRING,
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class GlucoseDataSingleView(generics.RetrieveAPIView):
    queryset = GlucoseData.objects.all()
    serializer_class = GlucoseDataSerializer
    lookup_field = "id"


class PrepopulateGlucoseData(APIView):
    def integerConversion(self, val):
        # Convert string to integer if possible
        if val.isdigit():
            return int(val)
        else:
            return None

    # Swagger documentation for request body and responses
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["file"],
            properties={
                "file": openapi.Schema(
                    type=openapi.TYPE_FILE,
                    description="CSV file containing glucose data.",
                )
            },
        ),
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                description="Successfully prepopulated glucose data.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "status": openapi.Schema(
                            type=openapi.TYPE_STRING, description="Success."
                        )
                    },
                ),
            ),
            status.HTTP_400_BAD_REQUEST: "Bad request. Invalid file format or data.",
            status.HTTP_500_INTERNAL_SERVER_ERROR: "Internal server error.",
        },
    )
    def post(self, request, *args, **kwargs):
        try:
            serializer = GlucoseDataUploadSerializer(data=request.data)
            if serializer.is_valid():
                file = serializer.validated_data["file"]
                reader = StringIO(file.read().decode("utf-8"))
                user_id = request.FILES.get("file").name.split(".")[0]
                customer, created = Customer.objects.get_or_create(user_id=user_id)
                next(reader)
                next(reader)
                next(reader)
                glucose_data_list = []
                for row in reader:
                    row = row.replace("\r\n", "").split(",")
                    timestamp = row[2]
                    timestamp_obj = datetime.strptime(timestamp, "%d-%m-%Y %H:%M")
                    device_data = {"device_name": row[0], "serial_number": row[1]}
                    device, created = Device.objects.get_or_create(**device_data)

                    glucose_data_list.append(
                        GlucoseData(
                            user=customer,
                            device=device,
                            device_timestamp=timestamp_obj,
                            record_type=self.integerConversion(row[3]),
                            glucose_history=self.integerConversion(row[4]),
                            glucose_scan=self.integerConversion(row[5]),
                            non_numeric_rapid_acting_insulin=row[6],
                            rapid_acting_insulin=self.integerConversion(row[7]),
                            non_numeric_food_data=row[8],
                            carbohydrates_grams=self.integerConversion(row[9]),
                            carbohydrates_portions=self.integerConversion(row[10]),
                            non_numeric_depot_insulin=row[11],
                            depot_insulin=self.integerConversion(row[12]),
                            notes=row[13],
                            glucose_test_strips=self.integerConversion(row[14]),
                            ketone=self.integerConversion(row[15]),
                            meal_insulin=self.integerConversion(row[16]),
                            corrective_insulin=self.integerConversion(row[17]),
                            insulin_change_by_user=self.integerConversion(row[18]),
                        )
                    )
                GlucoseData.objects.bulk_create(glucose_data_list)
                return Response({"status": "success"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return Response(
                {"error": "An unexpected error occurred"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
