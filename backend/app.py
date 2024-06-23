from flask import Flask, jsonify
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
MODEL="gpt-4o"

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, welcome to the Flask app!"

@app.route('/question')
def question():
    completion = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "I have a person who says he is interested in Administrative and Clerical Work specifically in Data Entry. I need to understand if the person is actually interested and good at it?"},
        {"role": "user", "content": "Can you give me a simple question to understand if the person is actually interested and good at it? Only output the question, do not say anything else."}
    ]
    )
    
    response_content = completion.choices[0].message.content

    return jsonify({"response": response_content})

if __name__ == '__main__':
    app.run(debug=True)