from pprint import pprint
import requests


def test_post_method():
    url = "https://airportgap.dev-tester.com/api/airports"
    response = requests.get(url)
    code = response.status_code
    pprint(response.json())
    assert code == 200