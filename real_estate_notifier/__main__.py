from real_estate_notifier.loader import load
from real_estate_notifier.scraper import scrape
from real_estate_notifier.db import get_last_posts, update_last_posts
from real_estate_notifier.logic import select_posts_to_notify, get_new_last_posts
from real_estate_notifier.notifier import notify

FUNDA_URL = (
    "https://www.funda.nl/en/huur/amsterdam/straat-museumplein/1000-1500/+2km/"
    "sorteer-datum-af/"
)
# The number should be increased if the expectancy of posts being rented is too high or simply the market is too hot
LAST_POSTS_COUNT = 5

print("Real Estate Notifier started working.")
html = load(FUNDA_URL)
print("Webpage is loaded.")
posts = scrape(html)
print(f"Webpage is scraped. {len(posts)} many posts are found.")
last_posts = get_last_posts()
print("Last posts are fetched from the db.")
posts_to_notify = select_posts_to_notify(posts, last_posts)
print(f"{len(posts_to_notify)} many posts are new.")
new_last_posts = get_new_last_posts(posts, LAST_POSTS_COUNT)
update_last_posts(new_last_posts)
print("The db is updated with the latest posts.")
notify(posts_to_notify)
print("Notification is sent.")
print("Real Estate Notifier is finished.")
