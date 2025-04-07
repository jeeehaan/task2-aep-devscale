from django.urls import path

from .views import BankListView, BankCreateView

urlpatterns = [
    path("", BankListView.as_view(), name="index"),
    path("create/", BankCreateView.as_view(), name="create_bank")
]
