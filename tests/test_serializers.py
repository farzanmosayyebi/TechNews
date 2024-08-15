import lorem
from django.test import TestCase

from data import models
from service import serializers


class NewsSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        tag1 = models.Tag.objects.create(title = "tag1")
        tag2 = models.Tag.objects.create(title = "tag2")
        tag3 = models.Tag.objects.create(title = "tag3")

        news = models.News.objects.create(
            title = lorem.sentence(),
            text = lorem.text(),
            source = "www.somerandomsource.com",
        )
        news.tags.add(tag1, tag2, tag3)

    def setUp(self) -> None:
        return super().setUp()
    
    def test_tags_are_retrieved_properly(self):
        news = models.News.objects.prefetch_related("tags").get(pk = 1)
        serializer = serializers.NewsSerializer(news)
        data = serializer.data.get("tags")
        assert "tag1" in data
        assert "tag2" in data 
        assert "tag3" in data
