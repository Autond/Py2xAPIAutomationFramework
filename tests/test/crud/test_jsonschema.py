# Get response
# create the json schema-jsonschema.net
# save that schema into the name.json file
# if you want to validate the json schema-jsonschemavalidator.net
import json

from jsonschema import validate
from jsonschema.exceptions import ValidationError
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import post_request
from src.helpers.common_verification import *
from src.helpers.payload_manager import payload_create_booking,payload_create_token
from src.utils.utils import Util

import pytest
import allure
import os

class TestCreateBookingJSONSchema(object):




    def load_schema(self,file_name):
        with open(file_name,'r') as file:
            return json.load(file)


    @pytest.mark.positive
    @allure.title("Verify Create Booking Status and Booking ID shouldn't be null")
    @allure.description("Creating a Booking from the payload and verify that Booking ID shouldn't be null and status code should be 200 for the correct payload")
    def test_create_booking_schema(self):
        # URL,Payload,headers
        payload = payload_create_token()
        response = post_request(url=APIConstants.url_create_booking(),
                                auth = None,
                                headers=Util().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)

        booking_id = response.json()["bookingid"]
        actual_status_code = response.status_code
        verify_http_status_code(response_data=response,expect_data=200)
        verify_json_key_for_not_null(booking_id)

        # compare response with schema.json that we have stored

        file_path= os.getcwd()+"/create_booking_schema.json"
        schema = self.load_schema(file_name=file_path)

        try:
            validate(instance=response.json(),schema=schema)# validate response with schema stored

        except ValidationError as e:
            print(e.message)
            pytest.xfail("incorrect") # to fail the test case in case of incorrect json,it gives warnings
            pytest.fail("Failed:json schema error") # to fail the test case,it gives red errors
