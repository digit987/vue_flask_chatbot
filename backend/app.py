from flask import Flask, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://vue-flask-chatbot.netlify.app/"}})

@app.route('/api/data')
def question_answer(question):
    #openai.api_key = ""

    messages=[{"role": "user", "content": question}]

    answer = openai.ChatCompletion.create(
      model="gpt-4",
      messages=messages,
      temperature=0.5,
      max_tokens=100,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )

    return jsonify({'message': answer['choices'][0]['message']['content']})

if __name__ == '__main__':
    app.run(debug=True)
