from ecommerce.inventory.models import Category


def test_create_category(single_category):
    new_category = single_category
    get_category = Category.objects.all().first()
    assert new_category.id == get_category.id


