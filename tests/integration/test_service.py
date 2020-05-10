"""
 File: test_service.py
 Description: pytest tests on the Falcon service 

 We are NOT going to exhaustively test the Calculator.compute() method
 as this is done in the unit-testing suite.
 Here, we are only concerned with testing the functionality of the Falcon service end-to-end.
 
"""
import pytest
import math
import json
from falcon import testing

from calculator import Calculator  

import app

headers = {"Content-Type": "application/json"}
##---------------------------------------------------------------------
@pytest.fixture()
    """
     Create the Falcon testClient() fixure. This will be used to send requests. 
    """
def client():
    return testing.TestClient(app.api)

## GET requests
def test_get_pi(client):
    """
     Check for expected json response
    """
    exp_resp = {'constant': 'pi', 'value': math.pi}
    req = '/calc/pi'
    result = client.simulate_get(req)
    assert result.json == exp_resp 

def test_get_tau(client):
    """
     Check for expected json response
    """
    exp_resp = {'constant': 'tau', 'value': math.tau}
    req = '/calc/tau'
    result = client.simulate_get(req)
    assert result.json == exp_resp 

## POST requests
def test_post_bad_route(client):
    """
     Check for status='404 Not Found' 
    """
    bad_path = '/calculus'
    exp_status = '404 Not Found' 
    result = client.simulate_post(path=bad_path, headers=headers)
    assert result.status == exp_status

def test_post_bad_payload(client):
    """
     Check for status='400 Bad Request' 
    """
    path = '/calc'
    exp_status = '400 Bad Request' 
    prob = '2+3'
    d_post = {'prob': prob}
    result = client.simulate_post(path=path, headers=headers, json=d_post)
    assert result.status == exp_status

def test_post_good(client):
    """
     Check for expected json response
    """
    path = '/calc'
    prob = '2+3'
    exp_resp = {'problem': prob, 'answer': 5.0}
    d_post = {'problem': prob}
    result = client.simulate_post(path=path, headers=headers, json=d_post)
    assert result.json == exp_resp 


