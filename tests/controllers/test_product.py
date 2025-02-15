from tests.factories import product_data
from fastapi import status


async def test_controller_create_should_return_success(client, products_url):
    response = await client.post(products_url, json=product_data())

    assert response.status_code == status.HTTP_201_CREATED


async def test_controller_get_should_return_success(
    client, products_url, product_inserted
):
    response = await client.get(f"{products_url}{product_inserted.id}")
    assert response.status_code == status.HTTP_200_OK


async def test_controller_get_should_return_not_found(client, products_url):
    response = await client.get(f"{products_url}fce6cc37-10b9-4r8e-a8b2-977df327001b")

    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_controller_query_should_return_success(client, products_url):
    response = await client.get(products_url)
    assert response.status_code == status.HTTP_200_OK


async def test_controller_patch_should_return_success(
    client, products_url, product_inserted
):
    response = await client.patch(
        f"{products_url}{product_inserted.id}", json={"quantity": 44}
    )
    assert response.status_code == status.HTTP_200_OK


async def test_controller_delete_should_return_no_content(
    client, products_url, product_inserted
):
    response = await client.delete(f"{products_url}{product_inserted.id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT
