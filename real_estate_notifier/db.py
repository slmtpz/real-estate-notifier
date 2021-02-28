from typing import List

import boto3

from .models import Post

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("real-estate-notifier-last-posts")


def get_last_posts() -> List[Post]:
    scan_results = table.scan()

    posts: List[Post] = []
    for item in scan_results["Items"]:
        del item["data"]
        del item["order"]
        posts.append(Post.parse_obj(item))

    return posts


def update_last_posts(last_posts: List[Post]):
    for i, last_post in enumerate(last_posts):
        item = {
            "data": "last-posts",
            "order": i + 1,
        }
        item.update(last_post.dict())
        table.put_item(Item=item)
