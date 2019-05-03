# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.payment.definitions.device_render_options import DeviceRenderOptions


class SdkDataInput(DataObject):

    __device_info = None
    __device_render_options = None
    __sdk_app_id = None
    __sdk_encrypted_data = None
    __sdk_ephemeral_public_key = None
    __sdk_max_timeout = None
    __sdk_reference_number = None
    __sdk_transaction_id = None

    @property
    def device_info(self):
        """
        | Device information gathered by the 3DS SDK on a customer device. This is JSON name/value pairs that as a whole is Base64url encoded.
        
        Type: str
        """
        return self.__device_info

    @device_info.setter
    def device_info(self, value):
        self.__device_info = value

    @property
    def device_render_options(self):
        """
        | Object containing rendering options of the device.
        
        Type: :class:`ingenico.connect.sdk.domain.payment.definitions.device_render_options.DeviceRenderOptions`
        """
        return self.__device_render_options

    @device_render_options.setter
    def device_render_options(self, value):
        self.__device_render_options = value

    @property
    def sdk_app_id(self):
        """
        | Universally unique ID created upon all installations and updates of your app on a c Device. This will be newly generated and stored by the 3DS SDK for each installation or update
        
        Type: str
        """
        return self.__sdk_app_id

    @sdk_app_id.setter
    def sdk_app_id(self, value):
        self.__sdk_app_id = value

    @property
    def sdk_encrypted_data(self):
        """
        | JWE Object containing data encrypted by the 3-D Secure SDK
        
        Type: str
        """
        return self.__sdk_encrypted_data

    @sdk_encrypted_data.setter
    def sdk_encrypted_data(self, value):
        self.__sdk_encrypted_data = value

    @property
    def sdk_ephemeral_public_key(self):
        """
        | Public key component of the ephemeral key pair generated by the 3-D Secure SDK and used to establish session keys between the 3-D Secure SDK and ACS.
        
        Type: str
        """
        return self.__sdk_ephemeral_public_key

    @sdk_ephemeral_public_key.setter
    def sdk_ephemeral_public_key(self, value):
        self.__sdk_ephemeral_public_key = value

    @property
    def sdk_max_timeout(self):
        """
        | Indicates maximum amount of time (in minutes) for all exchanges. Minimum amount of minutes is 5.
        
        Type: str
        """
        return self.__sdk_max_timeout

    @sdk_max_timeout.setter
    def sdk_max_timeout(self, value):
        self.__sdk_max_timeout = value

    @property
    def sdk_reference_number(self):
        """
        | Identifies the vendor and version for the 3-D Secure SDK that is integrated in your app, assigned by EMVCo when the 3-D Secure SDK is approved.
        
        Type: str
        """
        return self.__sdk_reference_number

    @sdk_reference_number.setter
    def sdk_reference_number(self, value):
        self.__sdk_reference_number = value

    @property
    def sdk_transaction_id(self):
        """
        | Universally unique transaction identifier assigned by the 3-D Secure SDK to identify a single transaction.
        
        Type: str
        """
        return self.__sdk_transaction_id

    @sdk_transaction_id.setter
    def sdk_transaction_id(self, value):
        self.__sdk_transaction_id = value

    def to_dictionary(self):
        dictionary = super(SdkDataInput, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'deviceInfo', self.device_info)
        self._add_to_dictionary(dictionary, 'deviceRenderOptions', self.device_render_options)
        self._add_to_dictionary(dictionary, 'sdkAppId', self.sdk_app_id)
        self._add_to_dictionary(dictionary, 'sdkEncryptedData', self.sdk_encrypted_data)
        self._add_to_dictionary(dictionary, 'sdkEphemeralPublicKey', self.sdk_ephemeral_public_key)
        self._add_to_dictionary(dictionary, 'sdkMaxTimeout', self.sdk_max_timeout)
        self._add_to_dictionary(dictionary, 'sdkReferenceNumber', self.sdk_reference_number)
        self._add_to_dictionary(dictionary, 'sdkTransactionId', self.sdk_transaction_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(SdkDataInput, self).from_dictionary(dictionary)
        if 'deviceInfo' in dictionary:
            self.device_info = dictionary['deviceInfo']
        if 'deviceRenderOptions' in dictionary:
            if not isinstance(dictionary['deviceRenderOptions'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['deviceRenderOptions']))
            value = DeviceRenderOptions()
            self.device_render_options = value.from_dictionary(dictionary['deviceRenderOptions'])
        if 'sdkAppId' in dictionary:
            self.sdk_app_id = dictionary['sdkAppId']
        if 'sdkEncryptedData' in dictionary:
            self.sdk_encrypted_data = dictionary['sdkEncryptedData']
        if 'sdkEphemeralPublicKey' in dictionary:
            self.sdk_ephemeral_public_key = dictionary['sdkEphemeralPublicKey']
        if 'sdkMaxTimeout' in dictionary:
            self.sdk_max_timeout = dictionary['sdkMaxTimeout']
        if 'sdkReferenceNumber' in dictionary:
            self.sdk_reference_number = dictionary['sdkReferenceNumber']
        if 'sdkTransactionId' in dictionary:
            self.sdk_transaction_id = dictionary['sdkTransactionId']
        return self
