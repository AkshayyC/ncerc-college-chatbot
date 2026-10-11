
import os
from pathlib import Path
from werkzeug.utils import secure_filename
from file_processor import extract_text_from_file
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    session,
    redirect,
    url_for,
)
from werkzeug.security import check_password_hash

# Load environment variables from the project's .env file.
load_dotenv(Path(__file__).with_name(".env"), override=True)

from database import (
    initialize_database,
    get_all_knowledge,
    add_knowledge,
    delete_knowledge,
)
from chatbot import generate_knowledge_draft
from chatbot import get_response


# ------------------------------
# Create the Flask application
# ------------------------------
app = Flask(__name__)
# Supported image and document formats
ALLOWED_UPLOAD_EXTENSIONS = {"pdf", "jpg", "jpeg", "png"}

# Maximum upload size: 10 MB
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

# Configure the session security key.
app.secret_key = os.environ.get("FLASK_SECRET_KEY")

if not app.secret_key:
    raise RuntimeError(
        "FLASK_SECRET_KEY is missing from your .env file."
    )


# Initialize the existing database without replacing its records.
initialize_database()


# ------------------------------
# Admin login
# ------------------------------
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "GET":
        if session.get("is_admin"):
            return redirect(url_for("admin_dashboard"))

        return render_template("admin_login.html")

    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    expected_username = os.environ.get("ADMIN_USERNAME", "")
    password_hash = os.environ.get("ADMIN_PASSWORD_HASH", "")

    if (
        expected_username
        and password_hash
        and username == expected_username
        and check_password_hash(password_hash, password)
    ):
        session["is_admin"] = True
        return redirect(url_for("admin_dashboard"))

    return (
        render_template(
            "admin_login.html",
            error="Invalid username or password.",
        ),
        401,
    )


# ------------------------------
# Protected admin dashboard
# ------------------------------
@app.route("/admin")
def admin_dashboard():
    if not session.get("is_admin"):
        return redirect(url_for("admin_login"))

    knowledge_items = get_all_knowledge()
    total_records = len(knowledge_items)

    categories = sorted({
        item["category"] for item in knowledge_items
    })
    total_categories = len(categories)

    return render_template(
        "admin_dashboard.html",
        total_records=total_records,
        total_categories=total_categories,
        categories=categories,
        knowledge_items=knowledge_items,
        admin_username=os.environ.get(
            "ADMIN_USERNAME", "ncerc_admin"
        ),
    )


#```python
# ------------------------------
# Generate an AI knowledge draft
# ------------------------------
@app.route("/admin/knowledge/draft", methods=["POST"])
def admin_generate_knowledge_draft():
    if not session.get("is_admin"):
        return redirect(url_for("admin_login"))

    source_text = request.form.get("source_text", "").strip()

    if not source_text:
        return "Please enter the college details first.", 400

    try:
        draft = generate_knowledge_draft(source_text)
    except Exception as error:
        print("KNOWLEDGE DRAFT ERROR:", error)
        return (
            "Could not generate a draft. Check the terminal for details.",
            500,
        )

    return render_template(
        "admin_draft_review.html",
        draft=draft,
        source_text=source_text,
    )

# Generate an AI knowledge draft from an uploaded file
@app.route("/admin/knowledge/upload-draft", methods=["POST"])
def admin_upload_knowledge_draft():
    if not session.get("is_admin"):
        return redirect(url_for("admin_login"))

    uploaded_file = request.files.get("file")

    if not uploaded_file or not uploaded_file.filename:
        return "Please select a PDF, JPG, or PNG file.", 400

    filename = secure_filename(uploaded_file.filename)
    extension = Path(filename).suffix.lower()

    if extension not in {".pdf", ".jpg", ".jpeg", ".png"}:
        return "Unsupported file type. Use PDF, JPG, or PNG.", 400

    try:
        source_text = extract_text_from_file(uploaded_file)

        if not source_text.strip():
            return "No readable text was found in the file.", 400

        draft = generate_knowledge_draft(source_text)

    except ValueError as error:
        return str(error), 400
    except Exception as error:
        print("FILE DRAFT ERROR:", error)
        return (
            "Could not process the file or generate a draft. "
            "Check the terminal for details.",
            500,
        )

    return render_template(
        "admin_draft_review.html",
        draft=draft,
        source_text=source_text,
    )

# Add a knowledge record
# ------------------------------
@app.route("/admin/knowledge/add", methods=["POST"])
def admin_add_knowledge():
    if not session.get("is_admin"):
        return redirect(url_for("admin_login"))

    category = request.form.get("category", "").strip()
    keywords = request.form.get("keywords", "").strip()
    answer = request.form.get("answer", "").strip()

    try:
        add_knowledge(category, keywords, answer)
    except ValueError as error:
        return str(error), 400

    return redirect(url_for("admin_dashboard"))

@app.route("/admin/knowledge/delete/<int:knowledge_id>", methods=["POST"])
def admin_delete_knowledge(knowledge_id):
    if not session.get("is_admin"):
        return redirect(url_for("admin_login"))

    deleted = delete_knowledge(knowledge_id)

    if not deleted:
        return "Knowledge record not found.", 404

    return redirect(url_for("admin_dashboard"))



# ------------------------------
# Admin logout
# ------------------------------
@app.route("/admin/logout")
def admin_logout():
    session.clear()
    return redirect(url_for("admin_login"))


# ------------------------------
# Existing student homepage
# ------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ------------------------------
# Existing chatbot API
# ------------------------------
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
        print("USER MESSAGE:", message)

        response = get_response(message)

        print("CHATBOT RESPONSE:", response)

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


# ------------------------------
# Run the application locally
# ------------------------------
if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000,
    )
