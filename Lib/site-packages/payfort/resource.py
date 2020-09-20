# -*- coding: utf-8 -*-
import requests

from payfort import api_base
from payfort.base import PayFortObject

__all__ = (
    "Card",
    "Charge",
    "Customer",
    "Refund",
    "Token"
)


class Card(PayFortObject):
    """
    When you create a new Card, you must specify a Customer to create it on.
    If the customer has no default card, then the new card will
    become the default.
    However, if the customer already has a default then it will not change.
    To change the default, you should update the customer and pass the new
    default_card_id.
    """
    url = api_base + "/customers"

    def create(self, customer_id, data):
        """
        Create a Card
        HTTP Request
        POST https://api.start.source.com/customers/{CUSTOMER_ID}/cards
        """
        return self.handle_response(requests.post(
            "%s/%s/cards" % (self.url, customer_id), data=data,
            auth=self.auth
        ))

    def retrieve(self, customer_id, card_id):
        """
        Retrieve a Card

        Just pass the unique card ID that you got when creating the Card
        and we’ll send you back the latest details on the card.

        HTTP Request

        GET https://api.start.source.com/customers/{CUSTOMER_ID}/cards/{CARD_ID}

        """
        return self.handle_response(requests.get(
            "%s/%s/cards/%s" % (self.url, customer_id, card_id),
            auth=self.auth
        ))

    def delete(self, customer_id, card_id):
        """
        Delete a Card

        This action permanently deletes a card.
        Previous transactions made using this card are not affected.

        HTTP Request

        DELETE https://api.start.source.com/customers/{CUSTOMER_ID}/cards/{CARD_ID}

        """
        return self.handle_response(requests.delete(
            "%s/%s/cards/%s" % (self.url, customer_id, card_id),
            auth=self.auth
        ))

    def get_all(self, customer_id):
        """
        List all Cards

        This endpoint returns a list of all of the cards for
        the specified customer.
        The cards are returned in sorted order, with the most recent cards
        appearing first.
        HTTP Request

        GET https://api.start.source.com/customers/{CUSTOMER_ID}/cards
        """
        return self.handle_response(requests.get(
            "%s/%s/cards" % (self.url, customer_id), auth=self.auth
        ))


class Token(PayFortObject):
    """
    You don’t want sensitive card information ending up on your servers.
    Therefore, it’s best to replace them (immediately) with a token.
    You do this by sending the Card details directly from the customers
     browser to our API .. so that the card details never touch your server.

    You can easily do this using our start.js library.

    Tokens are created with your open
    API key (yours is test_open_k_9091f35e42fe3cfc2ac9),
    which can safely be included in your client side source code,
    or in downloadable applications like iPhone/Android apps.
    Note that tokens should not be stored or used more than once —
    to store these details for use later, you should immediately
    create a Customer) from the token you get back.
    The Customer ID can then be stored and charged at
    a later time / multiple times.
    """

    url = api_base + '/tokens'

    def create(self, data):
        """
        Create a new Token
        You can create a token by making the following request:

        HTTP Request

        POST https://api.start.source.com/tokens/
        """
        return self.handle_response(
            requests.post(self.url, data=data, auth=self.auth, verify=True)
        )


class Charge(PayFortObject):
    """
    Charges

    To charge a credit or a debit card, you create a new charge object.
    You can retrieve and refund individual charges as well as list all charges.
    Charges are identified by a unique random ID
    (e.g. ch_913ac1cf34bb962d84f39f729ca4a).
    """
    url = api_base + "/charges"

    def create(self, data):
        """
        Create a new Charge
        This is where the action happens – creating a Charge is how you charge
        a credit / debit card with Start, and it’s really
        easy as you’ll see in a bit.

        HTTP Request

        POST https://api.start.source.com/charges/

        """
        return self.handle_response(
            requests.post(self.url, data=data, auth=self.auth)
        )

    def retrieve(self, charge_id):
        """
        Retrieve an existing Charge

        Just pass the unique Charge ID that you got when creating the
        Charge and we’ll send you back the latest details on the charge.

        HTTP Request

        GET https://api.start.source.com/charges/{CHARGE_ID}
        """
        return requests.get("%s/%s" % (self.url, charge_id),
                            auth=self.auth)

    def capture(self, charge_id, data):
        """
        Capture a Charge
        This step only applies to Authorizations (i.e. charges originally created with capture=false).

        Uncaptured payments expire exactly seven days after they are created. If they are not captured by that point, then they will be marked as refunded and can no longer be captured.
        HTTP Request

        POST https://api.start.source.com/charges/{CHARGE_ID}/capture
        """
        return requests.post(
            "%s/%s/capture" % (self.url, charge_id), data=data,
            auth=self.auth
        )

    def get_all(self):
        """
        List all Charges

        This endpoint retrieves all the charges that you’ve got on your account.
        That’s right .. all of it. The good, the bad and the ugly.
        (The failed and the successful charges).

        The charges are returned in sorted order,
        with the most recent charges appearing first.

        HTTP Request

        GET https://api.start.source.com/charges/
        """
        return requests.get(self.url, auth=self.auth)


class Customer(PayFortObject):
    URL = api_base + "/customers"

    def create(self, data):
        return self.handle_response(
            requests.post(self.URL, data=data, auth=self.auth))

    def get(self, customer_id):
        return self.handle_response(
            requests.get("%s/%s" % (self.URL, customer_id), auth=self.auth))

    def update(self, customer_id, data):
        return self.handle_response(
            requests.put("%s/%s" % (self.URL, customer_id),
                         data=data,
                         auth=self.auth))

    def delete(self, customer_id):  # Currently unavailable
        return self.handle_response(requests.delete(
            "%s/%s" % (self.URL, customer_id), auth=self.auth))

    def get_all(self):
        return self.handle_response(requests.get(self.URL, auth=self.auth))


class Refund(PayFortObject):
    url = api_base + "/charges"

    def create(self, charge_id, data):
        return self.handle_response(requests.post(
            "%s/%s/refunds" % (self.url, charge_id), data=data,
            auth=self.auth
        ))

    def get_all(self, charge_id):
        return self.handle_response(
            requests.get("%s/%s/refunds" % (self.url, charge_id),
                         auth=self.auth))
