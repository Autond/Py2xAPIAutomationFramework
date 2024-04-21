# Create token
# create booking id
# update the booking(put)-booking id,token
# delete the booking

# verify that we are able to update and delete the booking id

# create token
# create booking
# test_update --> fixtures (pass the data in pytest)

from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util

import pytest
import allure
import logging


class TestCRUDBooking(object):

    @allure.title("Test CRUD operation Update(PUT)")
    @allure.description("Verify full update with booking id and token")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = put_request(url=put_url,
                               headers=Util.common_header_put_delete_patch_cookie(self,token=token),
                               payload=payload_create_booking(),
                               auth=None,
                               in_json=False
                               )
        logger.info("Request is made"+ str(response))
        print(response.json())

        # Verifications
        #verify_json_key_for_not_null(response.json()["firstname"])
        #verify_json_key_for_not_null(response.json()["lastname"])
        verify_http_status_code(response_data=response, expect_data=200)
        #verify_response_key(response.json()["firstname"], expected_data="Amit")  # we can verify value this way

    @allure.title("Test CRUD operation Delete(delete)")
    @allure.description("Verify that delete operation is working")
    def test_delete_booking_id(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        delete_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = delete_request(
            url=delete_url,
            headers=Util().common_header_put_delete_patch_cookie(token=token),
            auth=None,
            in_json=False
        )
        print(response.text)
        verify_http_status_code(response_data=response, expect_data=201)
        verify_response_delete(response=response.text)
