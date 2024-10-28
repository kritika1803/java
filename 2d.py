def test_list_all_products():
    products = [create_fake_product() for _ in range(5)]
    for product in products:
        add_product_to_db(product)
    
    all_products = list_all_products()
    assert len(all_products) == len(products)
