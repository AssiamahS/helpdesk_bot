from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple knowledge base for helpdesk bot
knowledge_base = {
    "how do i reload a webpage with 1 or 2 key presses ( no mouse)": "Use Control/Command + R or F5"
    # Add more entries as needed
}

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get("question", "").lower()
    answer = knowledge_base.get(question, "I'm not sure how to help with that.")
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
