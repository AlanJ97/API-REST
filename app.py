from flask import Flask, jsonify
from products import products

app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})

@app.route('/products', methods=['GET'])
if __name__ == '__main__':
    app.run(debug=True, port=4000)
