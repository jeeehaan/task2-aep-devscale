from django.shortcuts import render
from django.views.generic import ListView
from apps.banks.models import Bank

class BankListView(ListView):
    model = Bank
    template_name = 'bank_list.html'
    context_object_name = 'banks'
