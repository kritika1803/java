def test_find_product_by_name():
    product = create_fake_product()
    add_product_to_db(product)
    
    result = find_product_by_name(product['name'])
    assert result['id'] == product['id']
