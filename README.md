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



