from flask import Flask, render_template, request, redirect, url_for, session, send_file
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from weasyprint import HTML
import io

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Database setup
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Create tables
with app.app_context():
    db.create_all()

# Home route
@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/home")
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return redirect(url_for("form"))

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])
        if User.query.filter_by(username=username).first():
            return "Username already exists!"
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            return redirect(url_for("form"))
        return "Invalid credentials!"
    return render_template("login.html")

# Logout
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login"))

# Resume form page
@app.route("/form", methods=["GET", "POST"])
def form():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("form.html")

# Saved resumes page
@app.route("/saved_resumes")
def saved_resumes():
    if "user_id" not in session:
        return redirect(url_for("login"))
    # For now, return empty list - you can implement file listing later
    return render_template("saved_resumes.html", files=[])

# Generate PDF with chosen template
@app.route("/generate_pdf", methods=["POST"])
def generate_pdf():
    if "user_id" not in session:
        return redirect(url_for("login"))

    data = request.form.to_dict(flat=False)
    template_choice = data.get("template", ["template1.html"])[0]
    
    # Process experiences text into structured format
    experiences_text = data.get("experiences", [""])[0]
    experiences = []
    if experiences_text:
        for line in experiences_text.split('\n'):
            line = line.strip()
            if line:
                experiences.append({
                    'position': line,
                    'employer': '',
                    'dates': '',
                    'summary': line,
                    'skills': ''
                })

    rendered = render_template(
        template_choice,
        name=data.get("name", [""])[0],
        email=data.get("email", [""])[0],
        phone=data.get("phone", [""])[0],
        education=data.get("education", [""])[0],
        skills=data.get("skills", [""])[0],
        experiences=experiences,
    )

    pdf = HTML(string=rendered).write_pdf()
    return send_file(io.BytesIO(pdf), download_name="resume.pdf", as_attachment=True)

# Live Preview (AJAX fetch for instant updates)
@app.route("/preview", methods=["POST"])
def preview():
    data = request.form.to_dict(flat=False)
    template_choice = data.get("template", ["template1.html"])[0]
    
    # Process experiences text into structured format
    experiences_text = data.get("experiences", [""])[0]
    experiences = []
    if experiences_text:
        for line in experiences_text.split('\n'):
            line = line.strip()
            if line:
                experiences.append({
                    'position': line,
                    'employer': '',
                    'dates': '',
                    'summary': line,
                    'skills': ''
                })

    rendered = render_template(
        template_choice,
        name=data.get("name", [""])[0],
        email=data.get("email", [""])[0],
        phone=data.get("phone", [""])[0],
        education=data.get("education", [""])[0],
        skills=data.get("skills", [""])[0],
        experiences=experiences,
    )
    return rendered

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
