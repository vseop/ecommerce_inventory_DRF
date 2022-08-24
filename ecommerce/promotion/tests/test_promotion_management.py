from datetime import date, timedelta

import pytest
from ecommerce.promotion.models import Promotion
from ecommerce.promotion.tasks import promotion_prices


@pytest.mark.parametrize(
    "reduction, result",
    [
        (10, 90),
        (50, 50),
    ],
)
def test_promotion_price_reduction(reduction, result, celery_app, celery_worker, promotion_multi_variant):
    promotion_prices(reduction, promotion_multi_variant.id)
    new_price = Promotion.products_on_promotion.through.objects.get(promotion_id=promotion_multi_variant.id)
    assert new_price.promo_price == result
