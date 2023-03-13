import requests


def test_get_all_airports():
    response = requests.get('https://airportgap.dev-tester.com/api/airports')
    data = response.json().get('data')

    assert response.status_code == 200
    assert len(data) > 5


def test_get_airports_by_id():
    # arrange/GIVEN
    airport_id = "LAE"
    # action/WHEN
    response = requests.get(f'https://airportgap.dev-tester.com/api/airports/{airport_id}')
    data = response.json().get('data')
    data_airport = data["attributes"]
    # assertion/THEN
    assert response.status_code == 200
    assert data_airport["name"] == "Nadzab Airport"
    assert data_airport["city"] == "Nadzab"
    assert data_airport["country"] == "Papua New Guinea"
    assert data_airport["altitude"] == 239
    assert data_airport["timezone"] == "Pacific/Port_Moresby"


def test_get_airports_by_id_wrong_assert():
    """
    This one is to test how it's looks like when having error
    since we can not modify the response to be error, so what we can do is
    to make assertion is false
    """
    airport_id = "LAE"
    # action/WHEN
    response = requests.get(f'https://airportgap.dev-tester.com/api/airports/{airport_id}')
    data = response.json().get('data')
    data_airport = data["attributes"]
    # assertion/THEN
    assert response.status_code == 200
    assert data_airport["name"] == "Jakarta Airport"
