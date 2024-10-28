def test_read_route(client):
    product = create_fake_product()
    add_product_to_db(product)
    
    response = client.get(f'/products/{product["id"]}')
    assert response.status_code == 200
    assert response.json['name'] == product['name']
