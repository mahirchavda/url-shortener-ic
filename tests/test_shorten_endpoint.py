import pytest


def test_shorten_endpoint_success(client):
    res = client.post("/api/shorten", json={"url": "https://google.com"})
    assert res.json == {
        "short_url": "https://abc.com/mZmevP2",
        "url": "https://google.com",
    }


def test_shorten_endpoint_url_with_extra_spaces(client):
    res = client.post("/api/shorten", json={"url": "     https://google.com     "})
    assert res.status_code == 200
    assert res.json == {
        "short_url": "https://abc.com/mZmevP2",
        "url": "https://google.com",
    }


def test_shorten_endpoint_without_url_param(client):
    res = client.post("/api/shorten", json={"abc": "https://google.com"})
    assert res.status_code == 400
    assert res.json == {
        "message": {"url": "Missing required parameter in the JSON body"}
    }


def test_shorten_endpoint_empty_url(client):
    res = client.post("/api/shorten", json={"url": "   "})
    assert res.status_code == 400
    assert res.json == {"message": {"url": "Must not be empty string"}}
