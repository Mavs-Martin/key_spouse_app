from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary user data for login (for demonstration purposes)
users = {'keyspouse': 'password123'}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
        return redirect(url_for('directory'))
    else:
        return "Invalid credentials. Please try again."

@app.route('/directory')
def directory():
    return render_template('directory.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
