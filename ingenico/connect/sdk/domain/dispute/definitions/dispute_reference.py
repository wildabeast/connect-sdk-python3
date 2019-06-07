# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject


class DisputeReference(DataObject):

    __merchant_order_id = None
    __merchant_reference = None
    __payment_reference = None
    __provider_id = None
    __provider_reference = None

    @property
    def merchant_order_id(self):
        """
        | The merchant’s order ID of the transaction to which this dispute is linked.
        
        Type: str
        """
        return self.__merchant_order_id

    @merchant_order_id.setter
    def merchant_order_id(self, value):
        self.__merchant_order_id = value

    @property
    def merchant_reference(self):
        """
        | Your (unique) reference for the transaction that you can use to reconcile our report files.
        
        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value):
        self.__merchant_reference = value

    @property
    def payment_reference(self):
        """
        | Payment Reference generated by WebCollect.
        
        Type: str
        """
        return self.__payment_reference

    @payment_reference.setter
    def payment_reference(self, value):
        self.__payment_reference = value

    @property
    def provider_id(self):
        """
        | The numerical identifier of the Service Provider (Acquirer).
        
        Type: str
        """
        return self.__provider_id

    @provider_id.setter
    def provider_id(self, value):
        self.__provider_id = value

    @property
    def provider_reference(self):
        """
        | The Service Provider’s reference.
        
        Type: str
        """
        return self.__provider_reference

    @provider_reference.setter
    def provider_reference(self, value):
        self.__provider_reference = value

    def to_dictionary(self):
        dictionary = super(DisputeReference, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'merchantOrderId', self.merchant_order_id)
        self._add_to_dictionary(dictionary, 'merchantReference', self.merchant_reference)
        self._add_to_dictionary(dictionary, 'paymentReference', self.payment_reference)
        self._add_to_dictionary(dictionary, 'providerId', self.provider_id)
        self._add_to_dictionary(dictionary, 'providerReference', self.provider_reference)
        return dictionary

    def from_dictionary(self, dictionary):
        super(DisputeReference, self).from_dictionary(dictionary)
        if 'merchantOrderId' in dictionary:
            self.merchant_order_id = dictionary['merchantOrderId']
        if 'merchantReference' in dictionary:
            self.merchant_reference = dictionary['merchantReference']
        if 'paymentReference' in dictionary:
            self.payment_reference = dictionary['paymentReference']
        if 'providerId' in dictionary:
            self.provider_id = dictionary['providerId']
        if 'providerReference' in dictionary:
            self.provider_reference = dictionary['providerReference']
        return self