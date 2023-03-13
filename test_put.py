from os import read
from pprint import pprint
import requests
import json

def test_post_method():
    url = "https://restful-booker.herokuapp.com/booking/6994"

    query ={"Content-Type": "application/json",
            "Cookie" : "token=75c8727d4b01d17"}

    file = open("C:\\Users\\Adikrisna\\Documents\\Proses Belajar\\MPM API\\post_update.json","r")
    request_json = json.loads(file.read())
    response = requests.post(url,json=request_json, headers=query)
    Code = response.status_code
    assert Code == 200
    pprint(response.json())