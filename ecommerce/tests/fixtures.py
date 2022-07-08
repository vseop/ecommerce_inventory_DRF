import pytest
from django.contrib.auth.models import User
from django.core.management import call_command


@pytest.fixture
def create_admin_user(django_user_model):
    """
    Return admin user
    """
    return django_user_model.objects.create_superuser(
        "admin", "a@a.com", "password"
    )
