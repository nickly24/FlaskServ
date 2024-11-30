from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Hello, World!'})
@app.route('/api', methods=['GET'])
def api():
    return jsonify({'message': 'API is working'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)