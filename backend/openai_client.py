import os
from openai import OpenAI

def question_answer(question):
    
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    message = [
        {
            "role": "system",
            "content": ""
        },
        {
            "role": "user",
            "content": question
        }
    ]

    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=message,
      temperature=0.5,
      max_tokens=100,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )

    return response.choices[0].message.content.strip()