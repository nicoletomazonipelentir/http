from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_endpoint', methods=['GET'])
def get_endpoint():
    return jsonify(message='O GET funcinou'), 200

@app.route('/post_endpoint', methods=['POST'])
def post_endpoint():
    if 'Authorization' not in request.headers:
        return jsonify(message='Não tá autorizado, falta o cabeçalho'), 401

    return jsonify(message='POST funciona'), 200

@app.route('/forbidden', methods=['GET'])
def forbidden():
    return jsonify(message='Proibidoh'), 403

@app.route('/not_found', methods=['GET'])
def not_found():
    return jsonify(message='Não achei'), 404

@app.route('/internal_error', methods=['GET'])
def internal_error():
    return jsonify(message='Erro interno de servidor, culpa da aws'), 500

if __name__ == '__main__':
    app.run(debug=True)
