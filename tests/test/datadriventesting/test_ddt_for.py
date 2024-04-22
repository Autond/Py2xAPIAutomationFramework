# Read the CSV or EXCEL FILE
# Create a function create_token which can take values from the Excel file
# Verify the Expected file
# Read the Excel-openpyxl

import openpyxl
import requests
from src.constants.api_constants import APIConstants
from src.helpers.api_request_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util

import pytest
import allure


def read_credentials_from_excel(file_path):  # it will give data from excel
    credentials = []
    workbook = openpyxl.load_workbook(filename=file_path)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append(({
            "username": username,
            "password": password

        }))
    return credentials


def create_auth_request(username, password):  # this will run the  no of times the rows are there in above function
    payload = {
        "username": username,
        "password": password
    }
    response = post_request(url=APIConstants.url_create_token(),
                            headers=Util.common_headers_json(self=None),
                            auth=None,
                            payload=payload,
                            in_json=False
                            )
    return response


def test_create_auth_with_excel():  # we will write the logic to run above function
    file_path = "C:\\Users\\acera\\PycharmProjects\\Py2xAPIAutomationFramework\\tests\\test\\datadriventesting\\testdata_ddt_123.xlsx"
    credentials = read_credentials_from_excel(file_path=file_path)
    print(credentials)
    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)
        response = create_auth_request(username=username, password=password)
        print(response.status_code)

    # def create_token(self):
    #     response = post_request(url=APIConstants.url_create_token(),
    #                             headers=Util.common_headers_json(self),
    #                             auth = None,
    #                             payload=payload_create_token(),
    #                             in_json= False
    #                             )
    #     verify_http_status_code(response_data=response,expect_data=200)
    #     verify_json_key_for_not_null_token(response.json()["token"])
    #     return response.json()["token"]
