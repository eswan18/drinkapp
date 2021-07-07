'''
This module runs a full workflow through the API and violates most principles of good testing.
'''

from fastapi.testclient import TestClient

from drinkapi.main import app

from .models.test_drink import near_equal

client = TestClient(app)


def test_workflow():
    # Insert a new user.
    user_json = {
        'username': 'eswan18',
        'wt_grams': 86183,
        'sex': 'male'
    }
    response = client.post('/user/', json=user_json)
    assert response.status_code == 201
    post_resp_json = response.json()
    user_id = post_resp_json['user_id']

    # Check that we can look up the user by ID.
    response = client.get(f'/user/{user_id}')
    assert response.status_code == 200
    get_resp_json = response.json()
    # We should get exactly the same content back as we did from the GET request.
    assert post_resp_json == get_resp_json

    # Record this user taking 1 double-size drink and 1 single-size drink.
    drinks = [{'drink_grams': grams, 'user_id': user_id}
              for grams in (28, 14)]
    for drink_json in drinks:
        response = client.post('/drink/', params=drink_json)
        assert response.status_code == 201

    # Make sure the user's current BAC is what we'd expect, via GET /drinks/
    response = client.get(f'/drink/{user_id}')
    assert response.status_code == 200
    bac = response.json()['bac']
    assert near_equal(bac, 0.071667)
