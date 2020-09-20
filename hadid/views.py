from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PaymentSerializer
from .models import Payment, Transaction
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
from django.http import HttpResponse
import cgi
import html
from django.views.decorators.csrf import csrf_exempt


def home_screen_view(request):
    context = {'merchant_identifier': Payment.merchant_identifier}

    return render(request, "templates/redirect.html", context)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all().order_by('merchant_identifier')
    serializer_class = PaymentSerializer


def initiate_payment(request):
    if request.method == "GET":
        return render(request, 'templates/pay.html')
    try:
        username = request.POST['username']
        password = request.POST['password']
        amount = int(request.POST['amount'])
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise ValueError
        auth_login(request=request, user=user)

    except:
        return render(request, 'templates/pay.html', context={'error': 'Wrong Account Details or amount'})

    transaction = Transaction.objects.create(made_by=user, amount=amount)
    transaction.save()

    requestParams = {
        'command': settings.COMMAND,
        'merchant_identifier': settings.MERCHANT_IDENTIFIER,
        'merchant_reference': settings.MERCHANT_REFERENCE,
        'currency': settings.CURRENCY,
        'language': settings.LANGUAGE,
        'access_code': settings.ACCESS_CODE,
        'customer_email': settings.CUSTOMER_EMAIL,
        'order_description': settings.ORDER_DESCRIPTION,
    }

    redirectUrl = 'https://sbcheckout.payfort.com/FortAPI/paymentPage'
    print(HttpResponse("<html xmlns='https://www.w3.org/1999/xhtml'>\n<head></head>\n<body>\n"))
    print("<form action='redirectUrl' method='post' name='frm'>\n")
    for (key, value) in requestParams.items():
        print("\t<input type='hidden' name='" + html.escape(key) + "' value='" + html.escape(value) + "'>\n")

    print("</form>")
    print("\t<script type='text/javascript'>\n")
    print("\t\tdocument.frm.submit();\n")
    print("\t</script>\n")
    print("\n</body>\n</html>")


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        requestParams = {}
        received_data['message'] = 'Checksum matched'

        return render(request, 'templates/callback.html', context=received_data)

# ModelViewSet is a special view that Django Rest Framework provides. It will handle GET and POST for Payment without
# us having to do any more work.
