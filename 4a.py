@app.route('/products/<int:id>', methods=['GET'])
def read_product(id):
    product = get_product_by_id(id)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404
