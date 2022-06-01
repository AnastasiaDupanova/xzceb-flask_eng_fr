from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french():
    text_to_translate = request.args.get('text_to_translate')
    text = translator.english_to_french(text_to_translate)
    return "Translated text to French" + text

@app.route("/french_to_english")
def frenchToEnglish():
    text_to_translate = request.args.get('text_to_translate')
    text1 = translator.french_to_english(text_to_translate)
    return "Translated text to English" + text1

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
