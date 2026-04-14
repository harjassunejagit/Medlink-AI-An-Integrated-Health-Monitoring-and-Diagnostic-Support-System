from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from config import Config
import bcrypt
import os

# Import utility functions
from utils.chatbot import chatbot_response
from utils.predictor import predict_disease
from utils.location import get_nearby_places
from utils.report import analyze_report

# ---------------- APP CONFIG ----------------

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "/"

# Create upload folder if not exists
if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])

# ---------------- DATABASE MODEL ----------------

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default="user")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ---------------- AUTH ROUTES ----------------

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/register", methods=["GET"])
def register_page():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    hashed_pw = bcrypt.hashpw(request.form["password"].encode(), bcrypt.gensalt())
    user = User(
        username=request.form["username"],
        email=request.form["email"],
        password=hashed_pw
    )
    db.session.add(user)
    db.session.commit()
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    user = User.query.filter_by(email=request.form["email"]).first()
    if user and bcrypt.checkpw(request.form["password"].encode(), user.password):
        login_user(user)
        return redirect("/dashboard")
    return "Invalid Credentials"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

# ---------------- CHATBOT ----------------

@app.route("/chatbot")
@login_required
def chatbot_page():
    return render_template("chatbot.html")

@app.route("/chat", methods=["POST"])
@login_required
def chat():
    message = request.json["message"]
    response = chatbot_response(message)
    return jsonify({"response": response})

# ---------------- DISEASE PREDICTION ----------------

@app.route("/predict_page")
@login_required
def predict_page():
    return render_template("predict.html")

@app.route("/predict", methods=["POST"])
@login_required
def predict():
    result = predict_disease(request.json)
    return jsonify(result)

# ---------------- REPORT ANALYSIS ----------------

# ---------------- REPORT ANALYSIS ----------------

@app.route("/report_page")
@login_required
def report_page():
    return render_template("report.html")


@app.route("/analyze_report", methods=["POST"])
@login_required
def analyze_report_route():

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    result = analyze_report(filepath)

    return jsonify(result)

# ---------------- LOCATION SERVICE ----------------
@app.route("/nearby_page")
@login_required
def nearby_page():
    return render_template("nearby.html")


@app.route("/nearby", methods=["POST"])
@login_required
def nearby():
    data = request.json

    radius = int(data.get("radius", 10))
    hospital_type = data.get("hospital_type", "all")

    places = get_nearby_places(
        float(data["lat"]),
        float(data["lng"]),
        radius,
        hospital_type
    )

    return jsonify(places)
# ---------------- ADMIN PANEL ----------------

@app.route("/admin")
@login_required
def admin():
    if current_user.role != "admin":
        return "Unauthorized"
    users = User.query.all()
    return render_template("admin.html", users=users)

# ---------------- MAIN ----------------

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
