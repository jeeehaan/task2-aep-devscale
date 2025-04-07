from django.urls import path

from .views import BankListView, BankCreateView

urlpatterns = [
    path("", BankListView.as_view(), name="bank"),
    path("create/", BankCreateView.as_view(), name="create_bank")
]
