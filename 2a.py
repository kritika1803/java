def test_read_product():
    product = create_fake_product()
    # Assume you have a function to add the product to the database
    add_product_to_db(product)
    
    result = read_product(product['id'])
    assert result['name'] == product['name']
