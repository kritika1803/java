def test_delete_route(client):
    product = create_fake_product()
    add_product_to_db(product)
    
    response = client.delete(f'/products/{product["id"]}')
    assert response.status_code == 204
