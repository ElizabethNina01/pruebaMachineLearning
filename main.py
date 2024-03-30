from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Agrega tu API key aquí
api_key = "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"

# Crea una instancia del cliente de OpenAI con tu API key
client = OpenAI(api_key=api_key)

@app.route('/generate', methods=['POST'])
def generate_response():
    prompt = request.json['prompt']
    response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal:socialbullyalert3:97z66Ua9",
        messages=[{"role": "user", "content": prompt}]
    )
    return jsonify({"response": response.choices[0].message.content})

if __name__ == '__main__':
    app.run()