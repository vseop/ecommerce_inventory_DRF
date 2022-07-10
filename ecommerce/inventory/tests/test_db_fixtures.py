import pytest
# from django.db import IntegrityError
from ecommerce.inventory import models


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", 1),
        (18, "trainers", "trainers", 1),
        (35, "baseball", "baseball", 1),
    ],
)
def test_inventory_category_dbfixture(
        db, db_fixture_setup, id, name, slug, is_active
):
    result = models.Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.parametrize(
    "slug, is_active",
    [
        ("fashion", 1),
        ("trainers", 1),
        ("baseball", 1),
    ],
)
def test_inventory_db_category_insert_data(
        db, category_factory, slug, is_active
):
    result = category_factory.create(slug=slug, is_active=is_active)
    print(result.name)
    assert result.slug == slug
    assert result.is_active == is_active
