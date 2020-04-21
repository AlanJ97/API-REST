from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})


@app.route('/products', methods=['GET'])
def get_producto():
    return jsonify({"products": products})


@app.route('/product/<string:product_name>', methods=['GET'])
def get_product(product_name):
    product_found = [product for product in products if product['name'] == product_name]
    if (len(product_found) > 0):

        return jsonify({'product': product_found[0]})
    else:
        return jsonify({'mensaje': "El objeto no existe"})


@app.route('/products', methods=['POST'])
def agregar_producto():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "Producto agregado", "Productos": products})


@app.route('/products/<string:product_name>', methods=['PUT'])
def edit_product(product_name):
    product_found = [product for product in products if product['name'] == product_name]
    if (len(product_found) > 0):
        product_found[0]['name'] = request.json['name'],
        product_found[0]['price'] = request.json['price'],
        product_found[0]['quantiy'] = request.json['quantity']
        return jsonify({
            "message": "Producto actualizado",
            "producto": product_found[0]
        })
    return jsonify({"message": "Producto no existente"})


# DELETE Data Route
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            'message': 'Product Deleted',
            'products': products
        })


if __name__ == '__main__':
    app.run(debug=True, port=4000)
