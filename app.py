from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route("/projects")
def projects():
    try:
        data = pd.read_csv("projects.csv")
        projects = data.to_dict(orient="records")
    except:
        projects = []

    return render_template("projects.html", projects=projects)

# Home page (dashboard)
@app.route("/")
def home():
    return render_template("index.html")


# Generate QR codes
@app.route("/generate")
def generate():
    os.system("python qr_generate.py")
    return "QR Codes Generated Successfully"


# Scan QR code
@app.route("/scan")
def scan():
    os.system("python qr_scan.py")
    return "QR Scanner Started"


# Validate QR
@app.route("/validate")
def validate():
    os.system("python qr_validate.py")
    return "QR Validation Started"


# Register Face
@app.route("/register")
def register():
    os.system("python face_register.py")
    return "Face Registration Started"


# Face Match (Attendance)
@app.route("/facematch")
def facematch():
    os.system("python face_match.py")
    return "Face Matching Started"


if __name__ == "__main__":
    app.run(debug=True)