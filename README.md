# Payfort-Django-Integration
Creating a Django based api with Payment Gateway integration to Payfort 
Before Starting the Integration section in the API:
Step 1: Access your test account
You have to make sure that you get access to a test account, it’s a full test environment allow you to simulate and process simulation transactions. You can contact support@payfort.com to get your test account.

Step 2: make sure that you are using the correct integration type
Before building the integration, you need to make sure that you are selecting and using the proper parameters in the API calls as per the required integration type.

Redirection
Authorization and Purchase
Operations that help the Merchant to complete the payment process. The Authorization operation hold an amount from the Customer’s credit card account for a period of time until the Merchant capture or void the transaction. If no capture or void was processed during this period, the transaction will be voided automatically. In Purchase you will send one single request in order to authorize and capture the transaction amount.

Authorization/ Purchase URLs
Test Environment URL:

https://sbcheckout.payfort.com/FortAPI/paymentPage

Production Environment URL:

https://checkout.payfort.com/FortAPI/paymentPage

Parameters Submission Type
HTTPs Form Post Request.

<form method=“post” action=“https://sbcheckout.payfort.com/FortAPI/paymentPage” id=“form1” name=“form1”> </form>

Authorization/ Purchase Request Example

import cgi

requestParams = {
'command' => 'AUTHORIZATION',
'access_code' => 'zx0IPmPy5jp1vAz8Kpg7',
'merchant_identifier' => 'CycHZxVj',
'merchant_reference' => 'XYZ9239-yu898',
'amount' => '10000',
'currency' => 'AED',
'language' => 'en',
'customer_email' => 'test@payfort.com',
'signature' => '7cad05f0212ed933c9a5d5dffa31661acf2c827a',
'order_description' => 'iPhone 6-S',
};


redirectUrl = 'https://sbcheckout.payfort.com/FortAPI/paymentPage';
print "<html xmlns='https://www.w3.org/1999/xhtml'>\n<head></head>\n<body>\n";
print "<form action='redirectUrl' method='post' name='frm'>\n";
for (slug, title) in requestParams.items():
    print "\t<input type='hidden' name='"+ cgi.escape(slug)+"' value='"+ cgi.escape(title)+"'>\n";

print "</form>";
print "\t<script type='text/javascript'>\n";
print "\t\tdocument.frm.submit();\n";
print "\t</script>\n";
print "\n</body>\n</html>";


Authorization/ Purchase Response Example

{"command":"AUTHORIZATION","access_code":"zx0IPmPy5jp1vAz8Kpg7","merchant_identifier":"CycHZxVj","merchant_reference":"XYZ9239-yu898","amount":"10000","currency":"AED","language":"en","customer_email":"test@payfort.com","signature":"7cad05f0212ed933c9a5d5dffa31661acf2c827a","fort_id":"149295435400084008","payment_option":"VISA","eci":"ECOMMERCE","order_description":"iPhone6-S","customer_ip":"192.178.1.10","customer_name":"John","response_message":"Success","response_code":"20064","status":"04","card_holder_name":"John Smith","expiry_date":"2105","card_number":"400555******0001"}
