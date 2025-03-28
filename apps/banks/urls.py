from django.urls import path

from .views import BankListView

urlpatterns = [
    path('', BankListView.as_view(), name='bank-list')
]