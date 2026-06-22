from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key="OPENROUTER_API_KEY",
    base_url="https://openrouter.ai/api/v1"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json.get("message")

    try:

        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are Vansh AI, the portfolio assistant of Vansh Tanwar.

                    Skills:
                    - Python
                    - Flask
                    - DSA
                    - LeetCode
                    - AI Projects

                    Projects:
                    - Jarvis AI Assistant
                    - Custom Programming Language Interpreter
                    - Portfolio Website

                    Contact:
                    - GitHub: vansh1236

                    Only answer questions related to Vansh.
                    """
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            max_tokens=300
        )

        reply = response.choices[0].message.content

        return jsonify({
            "reply": reply
        })

    except Exception as e:
        return jsonify({
            "reply": f"Error: {str(e)}"
        })

if __name__ == "__main__":
    app.run(debug=True)