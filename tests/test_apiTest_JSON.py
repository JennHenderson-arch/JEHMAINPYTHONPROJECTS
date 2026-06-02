# test_apiTest_JSON
# This file contains test cases for API endpoints that return JSON responses.
# 20260527 - created by: Jennifer Henderson, ChatGPT, OpenAI

##NOTE: example.com is a placeholder domain and does not actually return the expected JSON responses. In a real test suite, you would replace "https://example.com" with the actual URL of the API you are testing, and ensure that the API is set up to return the expected responses for each endpoint. The tests are designed to check both successful and error scenarios for GET, POST, PUT, and DELETE requests, and they assert the status code, response content, and content type of the responses.

import requests
import pytest

@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.regression


def test_get_user_success():
    # Make the request
    response = requests.get("https://fake-json-api.mock.beeceptor.com/users")
    
    # Assert status code and content
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert data[0]["id"] == 1
    ##print(data)  #comment this out before  uploading to repo. This is debug only.


##additional standard test cases for a typical RESTful API that manages user resources. These tests cover scenarios such as retrieving a user that does not exist, creating a new user with valid and invalid data, updating an existing user, and deleting a user. Each test checks the status code, response content, and content type to ensure that the API behaves as expected in both success and error cases.    
""" def test_get_user_not_found():
    # Make the request
    response = requests.get("https://example.com/999")
    
    # Assert status code and content
    assert response.status_code == 404
    assert response.json()["error"] == "User not found"

def test_create_user_success():
    # Define the payload
    payload = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    # Make the request
    response = requests.post("https://example.com/users", json=payload)
    # Assert status code and content
    assert response.status_code == 201      
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"   
    assert "application/json" in response.headers["Content-Type"]

def test_create_user_invalid_data():
    # Define the payload with missing fields
    payload = {
        "name": "John Doe"
    }

    # Make the request
    response = requests.post("https://example.com/users", json=payload)
    
    # Assert status code and content
    assert response.status_code == 400
    assert response.json()["error"] == "Email is required"      
    assert "application/json" in response.headers["Content-Type"]

def test_update_user_success():
    # Define the payload
    payload = {
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }

    # Make the request
    response = requests.put("https://example.com/users/1", json=payload)
    # Assert status code and content
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["email"] == "jane.doe@example.com"
    assert "application/json" in response.headers["Content-Type"]

def test_update_user_not_found():
    # Define the payload
    payload = {
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }

    # Make the request
    response = requests.put("https://example.com/users/999", json=payload)

    # Assert status code and content
    assert response.status_code == 404
    assert response.json()["error"] == "User not found"
    assert "application/json" in response.headers["Content-Type"]       

def test_delete_user_success():
    # Make the request
    response = requests.delete("https://example.com/users/1")

    # Assert status code and content
    assert response.status_code == 204
    assert response.text == ""  
    assert "application/json" in response.headers["Content-Type"]   

def test_delete_user_not_found():
    # Make the request
    response = requests.delete("https://example.com/users/999")

    # Assert status code and content
    assert response.status_code == 404
    assert response.json()["error"] == "User not found"
    assert "application/json" in response.headers["Content-Type"]   
 """
