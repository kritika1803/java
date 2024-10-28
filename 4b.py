@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    product = update_product_in_db(id, data)
    return jsonify(product), 200
