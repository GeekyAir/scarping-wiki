from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("manage-excel/", views.ExcelListCreateAPIView.as_view(), name="ExcelListCreateAPIView"),
    path("manage-excel/create/", views.create_google_sheet, name="create_google_sheet"),
    path("manage-excel/<int:index>/", views.ExcelDetailAPIView.as_view(), name="ExcelDetailAPIView"),
]