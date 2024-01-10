from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Organization


class OrganizationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )

        cls.organization = Organization.objects.create(
            name="Test Organization",
            creator=cls.user,
            details="Test details",
        )

    def test_organization_model(self):
        self.assertEqual(self.organization.name, "Test Organization")
        self.assertEqual(self.organization.creator.username, "testuser")
        self.assertEqual(self.organization.details, "Test details")
        self.assertEqual(str(self.organization), "Test Organization")
        self.assertEqual(self.organization.get_absolute_url(),
                         "/organizations/1/")

    def test_home_url_exists_at_desired_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_organization_list_url_exists_at_desired_location(self):
        response = self.client.get("/organizations/")
        self.assertEqual(response.status_code, 200)

    def test_organization_listview(self):
        response = self.client.get(reverse("organization_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.organization.name)
        self.assertTemplateUsed(response, "organization_list.html")

    def test_organization_detailview(self):
        response = self.client.get(
            reverse("organization_detail", kwargs={"pk": self.organization.id})
        )
        no_response = self.client.get("organization/100000")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, self.organization.details)
        self.assertTemplateUsed(response, "organization_detail.html")
