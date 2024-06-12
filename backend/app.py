from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://vue-flask-chatbot.netlify.app/"}})

@app.route('/api/data')
def get_data():
    data = {'message': 'Hello from Flask backend!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
