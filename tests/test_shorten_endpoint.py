import pytest


def test_shorten_endpoint_success(client):
    res = client.post("/api/shorten", json={"url": "https://google.com"})
    assert res.json == {
        "short_url": "https://abc.com/mZmevP2",
        "url": "https://google.com",
    }
