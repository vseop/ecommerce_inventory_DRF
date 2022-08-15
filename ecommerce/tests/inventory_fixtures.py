import pytest
from ecommerce.inventory.models import (
    Category,
    Product,
)


@pytest.fixture
def single_category(db):
    return Category.objects.create(name="default", slug="default")


@pytest.fixture
def category_with_child(db):
    parent = Category.objects.create(name="parent", slug="parent")
    parent.children.create(name="child", slug="child")
    child = parent.children.first()
    return child


@pytest.fixture
def single_product(db, category_with_child):
    product = Product.objects.create(
        web_id="123456789",
        slug="default",
        name="default",
        category=category_with_child,
        is_active=True,
    )
    return product
