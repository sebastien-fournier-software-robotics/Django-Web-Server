from django.urls import reverse
from rest_framework.test import APITestCase

from part1.models import Url


class Part1TestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = Url.objects.create(
            id=1,
            url_string="https://facebook.com",
            domain_name="facebook.com",
            protocol="htttps",
            title="Facebook - log in or sign up",
            image=[],
            stylesheets=0,
        )

        Url.objects.create(
            id=10,
            url_string="https://en.wikipedia.org/wiki/Iron_Man",
            domain_name="en.wikipedia.org",
            protocol="https",
            title="Iron Man - Wikipedia",
            image=[
                "/static/images/icons/wikipedia.png",
                "/static/images/mobile/copyright/wikipedia-wordmark-en.svg",
                "/static/images/mobile/copyright/wikipedia-tagline-en.svg",
                "//upload.wikimedia.org/wikipedia/en/thumb/9/94/Symbol_support_vote.svg/19px-Symbol_support_vote.svg.png",
                "//upload.wikimedia.org/wikipedia/en/thumb/1/1b/Semi-protection-shackle.svg/20px-Semi-protection-shackle.svg.png",
                "//upload.wikimedia.org/wikipedia/en/thumb/4/47/Iron_Man_%28circa_2018%29.png/220px-Iron_Man_%28circa_2018%29.png",
            ],
            stylesheets=2,
        )
        pass


class TestUrl(Part1TestCase):
    def setUp(self):
        self.url = reverse("url-list")

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        expected = [
            {
                "id": url.id,
                "url_string": url.url_string,
                "domain_name": url.domain_name,
                "protocol": url.protocol,
                "title": url.title,
                "image": url.image,
                "stylesheets": url.stylesheets,
            }
            for url in Url.objects.all()
        ]
        self.assertEqual(response.json().get("results"), expected)

    def test_create(self):
        url_count = Url.objects.count()
        data = {
            "url_string": "https://example.com",
            "domain_name": "example.com",
            "protocol": "https",
            "title": "Example",
            "image": [],
            "stylesheets": 1,
        }
        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Url.objects.count(), url_count + 1)

        new_url = Url.objects.latest("id")
        print(data["url_string"])
        self.assertEqual(
            response.json(),
            {
                "id": new_url.id,
                "url_string": new_url.url_string,
                "domain_name": new_url.domain_name,
                "protocol": new_url.protocol,
                "title": new_url.title,
                "image": new_url.image,
                "stylesheets": new_url.stylesheets,
            },
        )

    def test_delete(self):
        url_count = Url.objects.count()
        url_id_to_delete = 1

        response = self.client.delete(
            reverse("url-detail", kwargs={"pk": url_id_to_delete})
        )

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Url.objects.count(), url_count - 1)

        with self.assertRaises(Url.DoesNotExist):
            Url.objects.get(pk=url_id_to_delete)
