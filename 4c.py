@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    delete_product_from_db(id)
    return '', 204
