from flask import Flask, render_template, request
from openai import OpenAI
from promts import generateEnglish, generateHungarian
import sys
import os

api_key = open("api_key", "r", encoding="utf-8").read()

client = OpenAI(api_key = api_key)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/generate')
def generate():
    item_name = request.args.get('item_name', None)
    item_material = request.args.get('item_material', None)
    item_attr1 = request.args.get('item_attr1', None)
    item_attr2 = request.args.get('item_attr2', None)
    length = request.args.get('length', None)
    language = request.args.get('language', None)
    temperature = request.args.get('temperature', None)
    model = request.args.get('model', None);

    for key in request.args:
        print(key + "\t\t\"" + request.args.get(key) + "\"", file=sys.stdout)


    user_content = ""

    if (item_name == ""):
        return "Please provide an item name!"
    
    if (model == ""):
        model = "gpt-3.5-turbo-0125"

    if (temperature == ""):
        temperature = 0.0
    else:
        try:
            temperature = float(temperature) / 100
        except Exception as ex:
            return "Failed to prase temperature! " + str(ex)

    if (language == 'eng'):
        user_content = generateEnglish(item_name, item_attr1, item_attr2, length, item_material)
    if (language == 'hun'):
        user_content = generateHungarian(item_name, item_attr1, item_attr2, length, item_material)


    print("Promt: " + user_content + "\nTemperature: " +  str(temperature) + "\nMax Tokens: ", file=sys.stdout)


    chat_completion = client.chat.completions.create(
    model=model,
    messages = [
        {
            "role" : "system",
            "content" : "You are designed to create item descriptions for webshops"
        },
        {
            "role" : "user", 
            "content" : user_content
        }
    ], 
        temperature=0,
        max_tokens=300
    )

    return chat_completion.choices[0].message.content

