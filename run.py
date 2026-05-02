from flask import render_template
from app import create_app
from app.extensions import db

# Create app
app = create_app()

# Create tables
with app.app_context():
    db.create_all()

# ================= ROUTES =================

# Login page (default)
@app.route("/")
def home():
    return render_template("login.html")


# Signup page
@app.route("/signup-page")
def signup_page():
    return render_template("signup.html")


# Dashboard (main app)
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)