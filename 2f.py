def test_find_product_by_category():
    product = create_fake_product()
    add_product_to_db(product)
    
    result = find_product_by_category(product['category'])
    assert product in result
