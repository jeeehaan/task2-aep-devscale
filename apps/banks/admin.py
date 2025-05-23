from django.contrib import admin
from .models import Bank


class BankAdmin(admin.ModelAdmin):
    list_display = ("name", "balance", "created_at")


admin.site.register(Bank, BankAdmin)
