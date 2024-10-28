@app.route('/products', methods=['GET'])
def list_products():
    products = get_all_products()
    return jsonify(products), 200
