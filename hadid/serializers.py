"""
here we have to
Import the Hero model
Import the REST Framework serializer
Create a new class that links the Hero with its serializer
"""

from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ('merchant_identifier', 'command', 'custname', 'date', 'amount', 'order_description', 'currency', 'customer_email',
                  'access_code', 'merchant_reference', 'language','signature')