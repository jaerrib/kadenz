from django.contrib.auth import get_user_model
from django.test import TestCase

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
