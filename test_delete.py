import requests
import json
import jsonpath
import pytest

def test_delete_method():
    url = "https://restful-booker.herokuapp.com/booking/806"
    
    query ={"Content-Type": "application/json",
            "Cookie" : "token=75c8727d4b01d17"}

    response = requests.delete(url, headers=query)
    Code = response.status_code
    assert Code == 200

    json_response = json.loads(response.text)
    nilai = jsonpath.jsonpath(json_response,"_value")
    assert nilai[0] == None