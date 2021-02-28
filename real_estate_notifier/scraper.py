from typing import List

from bs4 import BeautifulSoup

from .models import Post


FUNDA_BASE_URL = "https://www.funda.nl/en"


def scrape(html: str) -> List[Post]:
    soup = BeautifulSoup(html, features="html.parser")
    search_results = soup.find_all("li", {"class": "search-result"})

    return [
        Post(
            post_url=FUNDA_BASE_URL + search_result.find("div", {"class": "search-result-media"}).a["href"],
            image_url=search_result.find("div", {"class": "search-result-media"}).img["src"],
            title=search_result.find("div", {"class": "search-result__header"}).h2.text.strip(),
            address=search_result.find("div", {"class": "search-result__header"}).h4.text.strip(),
            price=search_result.find("span", {"class": "search-result-price"}).text.strip(),
            size=search_result.find("ul", {"class": "search-result-kenmerken"}).find_all("li")[0].text.strip(),
            rooms=search_result.find("ul", {"class": "search-result-kenmerken"}).find_all("li")[1].text.strip(),
        ) for search_result in search_results
    ]

