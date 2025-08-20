import requests
from bs4 import BeautifulSoup

def get_ptt_boards():
    url = "https://www.ptt.cc/bbs/index.html"
    response = requests.get(url = url)

    soup = BeautifulSoup(response.text, "html.parser")
    boards = soup.find_all(
        attrs = {"class": "board-name"},
        name = "div"
    )

    return [temp.text for temp in boards]

def get_my_method():
    return "Oops!!!"