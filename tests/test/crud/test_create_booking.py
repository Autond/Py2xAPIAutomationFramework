
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import post_request
from src.helpers.common_verification import *
from src.helpers.payload_manager import payload_create_booking,payload_create_token
from src.utils.utils import Util

import pytest
import allure
class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("Verify Create Booking Status and Booking ID shouldn't be null")
    @allure.description("Creating a Booking from the payload and verify that Booking ID shouldn't be null and status code should be 200 for the correct payload")
    def test_create_booking_positive(self):
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

    @pytest.mark.negative
    def test_create_booking_negative(self):
        # URL,Payload,headers
        response = post_request(url=APIConstants.url_create_booking(),
                                auth = None,
                                headers=Util().common_headers_json(),
                                payload={},
                                in_json=False)

        verify_http_status_code(response,500)


