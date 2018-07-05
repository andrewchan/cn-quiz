import requests
import pytest

@pytest.fixture
def get_auth():
    user = 'good_user'
    password = 'good_password'
    url = 'https://585c8698-9ca8-4582-852f-c5a8c52e2569.mock.pstmn.io/api/auth'

    return requests.post(url, data={'identity':user, 'credentials':password})

def test_auth_valid_user_and_password(get_auth):
    assert get_auth.status_code == 200
    token = get_auth.json()['token']
    
    assert token != ''
        
def test_auth_incorrect_password():
    user = 'good_user'
    password = 'incorrect_password'
    url = 'https://585c8698-9ca8-4582-852f-c5a8c52e2569.mock.pstmn.io/api/auth'

    r = requests.post(url, data={'identity':user, 'credentials':password}, headers={'X-Mock-Response-Code':'401'})
    assert r.status_code == 404

def test_auth_user_dont_exist():
    user = 'unknown'
    password = 'some_password'
    url = 'https://585c8698-9ca8-4582-852f-c5a8c52e2569.mock.pstmn.io/api/auth'

    r = requests.post(url, data={'identity':user, 'credentials':password}, headers={'X-Mock-Response-Code':'401'})
    assert r.status_code == 404

def test_profile_good_token(get_auth):
    profile_url = 'https://585c8698-9ca8-4582-852f-c5a8c52e2569.mock.pstmn.io/api/users/current'
    token = get_auth.json()['token']
    assert token != ''

    r = requests.get(profile_url, headers={'X-Auth-Token':token, 'X-Mock-Response-Code':'200'})
    assert r.status_code == 200
    assert r.json()['user_id'] == '12abc34'
    assert r.json()['date_of_birth'] == "1985-11-28"
    assert r.json()["followers_count"] == 123

def test_profile_missing_auth_header():
    profile_url = 'https://585c8698-9ca8-4582-852f-c5a8c52e2569.mock.pstmn.io/api/users/current'
    r = requests.get(profile_url, headers={'X-Mock-Response-Code':'401'})
    assert r.status_code == 401

def test_profile_missing_token():
    profile_url = 'https://585c8698-9ca8-4582-852f-c5a8c52e2569.mock.pstmn.io/api/users/current'
    r = requests.get(profile_url, headers={'X-Auth-Token':'', 'X-Mock-Response-Code':'401'})
    assert r.status_code == 401

def test_profile_bad_token():
    profile_url = 'https://585c8698-9ca8-4582-852f-c5a8c52e2569.mock.pstmn.io/api/users/current'
    r = requests.get(profile_url, headers={'X-Auth-Token':'bad_token', 'X-Mock-Response-Code':'401'})
    assert r.status_code == 401
