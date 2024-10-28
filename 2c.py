def test_delete_product():
    product = create_fake_product()
    add_product_to_db(product)
    
    delete_product(product['id'])
    assert read_product(product['id']) is None
