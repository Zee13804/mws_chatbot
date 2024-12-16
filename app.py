from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API Key
openai.api_key = "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"

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json['message']
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI assistant that provides information about MWS services like SEO, Google Ads, Social Media Management, and Web Development."},
            {"role": "user", "content": user_input}
        ]
    )
    bot_reply = response['choices'][0]['message']['content']
    return jsonify({"reply": bot_reply})

if __name__ == '__main__':
    app.run(port=5000)
