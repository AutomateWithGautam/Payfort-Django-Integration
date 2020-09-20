from django.db import models
from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()


class Payment(models.Model):
    merchant_identifier = models.CharField(max_length=20)
    custname = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    command = models.CharField(max_length=30, default='PURCHASE')
    order_description = models.TextField(default='iPhone 6-S')
    currency = models.CharField(max_length=40, default='AED')
    language = models.CharField(max_length=40, default='en')
    customer_email = models.EmailField(max_length=40, default='test@payfort.com')
    access_code = models.CharField(max_length=40, default="rxaCBohhRdmZopQxc4gu")
    merchant_reference = models.CharField(max_length=30, default="")
    signature = models.CharField(max_length=30, default="")

    def __str__(self):
        return '{}{}'.format(self.custname, self.order_description)


class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions',
                                on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)
