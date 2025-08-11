from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    # Get JSON data from request
    data = request.get_json()
    text = data.get('text', '') if data else ''
    translated_text = f"Translated version of: {text}"

    return jsonify({"translated_text": translated_text})

if __name__ == '__main__':
    app.run(debug=True)

   
