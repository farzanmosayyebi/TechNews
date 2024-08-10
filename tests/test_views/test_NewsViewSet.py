import lorem
from django.test import TestCase
from django.urls import reverse
from django.utils.http import urlencode

from api import views
from data import models


def reverse_querystring(view, urlconf=None, args=None, kwargs=None, current_app=None, query_kwargs=None):
    '''Custom reverse to handle query strings.
    Usage:
        reverse('app.views.my_view', kwargs={'pk': 123}, query_kwargs={'search': 'Bob'})
    '''
    base_url = reverse(view, urlconf=urlconf, args=args, kwargs=kwargs, current_app=current_app)
    if query_kwargs:
        return '{}?{}'.format(base_url, urlencode(query_kwargs))
    return base_url

class NewsViewSetTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        tag1 = models.Tag.objects.create(title="tag1")
        tag2 = models.Tag.objects.create(title="tag2")
        tag3 = models.Tag.objects.create(title="tag3")

        news1 = models.News.objects.create(
            title=lorem.sentence(),
            text = lorem.text(),
        )
        news1.tags.add(tag1, tag2)

        news2 = models.News.objects.create(
            title = lorem.sentence(),
            text = lorem.text(),
        )
        news2.tags.add(tag1)

        news3 = models.News.objects.create(
            title = lorem.sentence(),
            text = lorem.text(),
        )
        news3.tags.add(tag1, tag2, tag3)
    
    def setUp(self) -> None:
        return super().setUp()

    def test_news_list_format(self):
        response = self.client.get("/news/")
        self.assertEqual(response.status_code, 200)
    
    def test_news_list_filter_by_tag_1(self):
        tag = "some_irrelevant_tag"
        response = self.client.get(reverse_querystring("news-list", query_kwargs = {
            "tags": tag,
        },))

        news_with_irrelevant_tag_count = response.json().get("count")
        self.assertEqual(news_with_irrelevant_tag_count, 0)

    def test_news_list_filter_by_tag_2(self):
        tags = models.Tag.objects.filter(title__in = ["tag2", "tag3"]).only("title")
        tag_titles = ','.join([tag.title for tag in tags])
        response = self.client.get(reverse_querystring(
            "news-list", query_kwargs= {
                "tags": tag_titles
            }
        ))

        news_with_tag2_and_tag3_count = response.json().get("count")
        self.assertEqual(news_with_tag2_and_tag3_count, 2)

    def test_news_list_filter_by_tag_3(self):
        tag = models.Tag.objects.only("title").get(title="tag1")
        response = self.client.get(reverse_querystring(
            "news-list", query_kwargs= {
                "tags": tag.title
            }
        ))

        news_with_tag1_count = response.json().get("count")
        self.assertEqual(news_with_tag1_count, 3)

    def test_news_list_filter_by_tag_4(self):
        tag = models.Tag.objects.only("title").get(title="tag3")
        response = self.client.get(reverse_querystring(
            "news-list", query_kwargs= {
                "tags": tag.title
            }
        ))

        news_with_tag3_count = response.json().get("count")
        self.assertEqual(news_with_tag3_count, 1)

    def test_news_retrieve_status_code(self):
        response = self.client.get(reverse("news-detail", kwargs={
            "pk": 1,
        }))
        self.assertEqual(response.status_code, 200)