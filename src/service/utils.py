from django.db import transaction

from data import models


@transaction.atomic
def store_items_in_db(items):
    """
    Stores the received items in database.

    Creates `News` and `Tag` objects based on `items` and stores
    them in database.

    Parameters:
        items (list): List of dictionaries which `News` objects will be created from.
    """
    for item in items:
        news_object = models.News.objects.create(
            title = item["title"],
            text = item["text"],
            source = item["source"],
        )

        tags = []
        for tag in item["tags"]:
            tag_object, _ = models.Tag.objects.get_or_create(title = tag)
            tags.append(tag_object.id)
        news_object.tags.set(tags)
