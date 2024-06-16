from flask import Flask, request, jsonify
from flask_cors import CORS
from rag_client import invoke_rag_chain

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://vue-flask-chatbot.netlify.app"}})

@app.route('/api/data', methods=['POST'])
def get_data():
    message = request.json.get('message')
    response_message = jsonify({'message': invoke_rag_chain(message)})
    return response_message

if __name__ == '__main__':
    app.run(debug=True)