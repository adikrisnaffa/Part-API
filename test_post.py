from os import read
from pprint import pprint
import requests
import json
import pytest
import jsonpath

def test_post_method():
    url = "https://airportgap.dev-tester.com/api/airports"
    response = requests.get(url)
    code = response.status_code
    pprint(response.json())
    assert code == 200