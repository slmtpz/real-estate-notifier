from typing import List

from .models import Post


def select_posts_to_notify(
    current_posts: List[Post], last_posts: List[Post]
) -> List[Post]:
    """Determine the posts to be notified with.

    current_posts: N many posts that are sorted on date in descending order.
    last_posts: M many posts that are sorted on date in descending order.

    We want to return the current posts that are created after the last post. However,
    we cannot just depend on the very last post because the post might already have
    been removed from the site. Therefore, we have more than 1 "last posts" to check
    for each. If the iterated last post is found in the current posts, return the
    current posts before that post.
    """

    for last_post in last_posts:
        for i, current_post in enumerate(current_posts):
            if last_post.title == current_post.title:
                return current_posts[:i]

    return current_posts


def get_new_last_posts(posts: List[Post], count: int):
    """Determine the current last posts."""
    return posts[:count]
