import os

import requests


def load(url: str) -> str:
    """Get the source of a web page."""
    resp = requests.get(url, headers=_get_headers(), proxies=_get_proxies())

    return resp.text


def _get_headers() -> dict:
    """Instead of requests/Python's default user agent, use a normal user agent."""
    return {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
            " like Gecko) Chrome/88.0.4324.150 Safari/537.36"
        )
    }


def _get_proxies() -> dict:
    """Send the loading request over a proxy."""
    return {
        "https": os.environ.get("HTTPS_PROXY"),
        "http": os.environ.get("HTTPS_PROXY"),
    }


def _dump_to_file(text, name="dump"):
    with open(f"htmls/{name}.html", "w") as file:
        file.write(text)
