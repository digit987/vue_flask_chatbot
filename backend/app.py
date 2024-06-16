from flask import Flask, request, jsonify
from flask_cors import CORS
from OpenAIInteraction import question_answer

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

@app.route('/api/data', methods=['POST'])
def get_data():
    message = request.json.get('message')
    response_message = jsonify({'message': question_answer(message)})
    return response_message
