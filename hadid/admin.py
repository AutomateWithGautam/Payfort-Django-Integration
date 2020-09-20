# Register your models here.

from django.contrib import admin
from .models import Transaction,Payment


admin.site.register(Payment)

admin.site.register(Transaction)