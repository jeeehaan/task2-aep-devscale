from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from apps.banks.models import Bank
from apps.banks.tasks import task_do_something


class BankListView(ListView):
    model = Bank
    template_name = "index.html"
    context_object_name = "banks"

class BankCreateView(View):
    def get(self,request):
        return render(request,"create_bank.html")


    def post(self, request):
        bankname = request.POST.get("bankname")
        balance = request.POST.get("balance")

        task_do_something()
        Bank.objects.create(name=bankname, balance=balance, user=request.user)
        return redirect("bank")