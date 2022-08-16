import json




def test_get_product_by_category(api_client, single_product):
    product = single_product
    endpoint = f"/api/inventory/products/category/{product.category}/"
    response = api_client().get(endpoint)
    expected_json = [
        {
            "name": product.name,
            "web_id": product.web_id,
        }
    ]
    assert response.status_code == 200
    assert response.data == expected_json


#
