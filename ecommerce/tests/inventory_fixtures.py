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
def category_with_multiple_children(db):
    record = Category.objects.build_tree_nodes(
        {
            "id": 1,
            "name": "parent",
            "slug": "parent",
            "children": [
                {
                    "id": 2,
                    "parent_id": 1,
                    "name": "child",
                    "slug": "child",
                    "children": [
                        {
                            "id": 3,
                            "parent_id": 2,
                            "name": "grandchild",
                            "slug": "grandchild",
                        }
                    ],
                }
            ],
        }
    )
    category = Category.objects.bulk_create(record)
    return category


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
