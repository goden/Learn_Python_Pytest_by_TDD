import pytest
import requests
from fake_useragent import FakeUserAgent

@pytest.fixture(name='headers')
def headers_fixture() -> dict:
    fake_useragent = FakeUserAgent()

    return {"user-agent": fake_useragent.chrome}

def test_ptt_crawl(headers:dict):
    url = "https://www.ptt.cc/bbs/index.html"
    print(headers)

    res = requests.get(url, headers=headers)

    assert res.status_code == 200
    assert "Gossiping" in res.text
