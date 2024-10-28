def test_list_all_route(client):
    products = [create_fake_product() for _ in range(5)]
    for product in products:
        add_product_to_db(product)
    
    response = client.get('/products')
    assert response.status_code == 200
    assert len(response.json) == len(products)
