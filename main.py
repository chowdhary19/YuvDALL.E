from flask import Flask, jsonify
import os
from dotenv import load_dotenv
import openai
from flask import render_template

load_dotenv()

openai_api_key = os.getenv('KEY')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', )


@app.route('/generateimages/<prompt>')
def generate(prompt):
    print("prompt:", prompt)
    response = openai.images.generate(prompt=prompt, n=4, size="256x256")
    print(response)
    return jsonify(response)


app.run(host='0.0.0.0', port=81)
