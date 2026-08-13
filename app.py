from flask import Flask, render_template, request, jsonify

from database import initialize_database
from chatbot import get_response


app = Flask(__name__)


# Create the SQLite database and knowledge base
# when the application starts.
initialize_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "response": "Please enter a question."
        })

    message = data.get("message", "").strip()

    if not message:
        return jsonify({
            "response": "Please enter a question."
        })

    try:

        response = get_response(message)

        return jsonify({
            "response": response
        })

    except Exception as error:

        print("CHATBOT ERROR:", error)

        return jsonify({
            "response": (
                "Sorry, I couldn't process your question "
                "right now. Please try again."
            )
        }), 500


if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )