def test_find_product_by_availability():
    product = create_fake_product()
    add_product_to_db(product)
    
    result = find_product_by_availability(product['availability'])
    assert product in result
