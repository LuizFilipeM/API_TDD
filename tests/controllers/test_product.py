from tests.factories import product_data
from fastapi import status


async def test_controller_create_should_return_success(client, products_url):
    response = await client.post(products_url, json=product_data())

    assert response.status_code == status.HTTP_201_CREATED


async def test_controller_get_should_return_success(
    client, products_url, products_inserted
):
    await client.get(f"{products_url}{products_inserted.id}")
    # assert response.status_code == status.HTTP_201_CREATED
