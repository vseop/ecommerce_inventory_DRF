import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

fake = Faker()

from ecommerce.inventory import models


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    # name = fake.lexify(text='cat_name_??????')
    name = factory.Sequence(lambda n: f"cat_slug_{n}")  # если уникальное поле
    slug = fake.lexify(text="cat_slug_??????")


register(CategoryFactory)
