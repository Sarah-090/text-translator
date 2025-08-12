from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text', '') if data else ''
    translated_text = f"Translated version of: {text}"

    return jsonify({"translated_text": translated_text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Error loading template: {str(e)}"
