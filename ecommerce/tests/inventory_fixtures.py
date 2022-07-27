import pytest
from ecommerce.inventory.models import (

    Category,

)


@pytest.fixture
def single_category(db):
    return Category.objects.create(name="default", slug="default")


