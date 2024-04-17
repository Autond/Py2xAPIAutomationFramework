# class or function

import requests
import json


def get_request(url,auth,in_json):
    response = requests.get(url=url,auth=auth)
    return response.json()


def post_request(url,auth,headers,payload,in_json):
    post_response = requests.post(url=url,auth=auth,headers=headers,data=json.dumps(payload))
# whatever payload dictionary we are providing in json.dump is converted to json only
# in_json returns boolean value

    if in_json is True:
        return post_response.json()

    return post_response

def patch_request(url,auth,headers,payload,in_json):
    patch_response_data = requests.patch(url=url,auth=auth,headers=headers,data=json.dumps(payload))

    if in_json is True:
        return patch_response_data.json()
    return patch_response_data

def put_request(url,auth,headers,payload,in_json):
    put_response_data = requests.put(url=url,auth=auth,headers=headers,data=json.dumps(payload))

    if in_json is True:
        return put_response_data.json()
    return put_response_data


def delete_request(url,auth,headers,in_json):
    delete_response_data = requests.delete(url=url,auth=auth,headers=headers)

    if in_json is True:
        return delete_response_data.json()
    return delete_response_data

