import requests


def load(url: str) -> str:
    # [PRES] Try without user agent first. Dump and try with the user agent.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)

    return resp.text


def dump_to_file(text):
    with open("dump.html", "w") as file:
        file.write(text)
