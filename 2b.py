def test_update_product():
    product = create_fake_product()
    add_product_to_db(product)
    
    updated_data = {"name": "Updated Name"}
    update_product(product['id'], updated_data)
    
    updated_product = read_product(product['id'])
    assert updated_product['name'] == "Updated Name"
