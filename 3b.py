def test_update_route(client):
    product = create_fake_product()
    add_product_to_db(product)
    
    response = client.put(f'/products/{product["id"]}', json={"name": "Updated Name"})
    assert response.status_code == 200
    
    updated_product = read_product(product['id'])
    assert updated_product['name'] == "Updated Name"
