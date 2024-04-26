from django.urls import path

from .views import GlucoseDataListView, GlucoseDataSingleView, PrepopulateGlucoseData, GlucoseMinMaxView

urlpatterns = [
    path("v1/levels/", GlucoseDataListView.as_view(), name="glucose-data-list"),
    path(
        "v1/levels/<int:id>/",
        GlucoseDataSingleView.as_view(),
        name="glucose-data-single",
    ),
    path(
        "v1/prepopulate-data/",
        PrepopulateGlucoseData.as_view(),
        name="import-glucose-data",
    ),
    path(
        "v1/min-max-blood/",
        GlucoseMinMaxView.as_view(),
        name="minmax-glucose-data",
    ),
]
