from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

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
        session['username'] = username
        return redirect(url_for('statement'))
    else:
        return "Invalid credentials. Please try again."

@app.route('/statement')
def statement():
    if 'username' not in session:
        return redirect(url_for('home'))
    return render_template('statement.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/tricare')
def tricare():
    return redirect("https://www.tricare-west.com/content/hnfs/home/tw.html")

@app.route('/commissary')
def commissary():
    return redirect("https://www.commissaries.com/shopping/store-locations/davis-monthan-afb")

@app.route('/fss')
def fss():
    return redirect("https://www.dmfss.com/")

@app.route('/workout')
def workout():
    return "<h1>Workout</h1>"

@app.route('/meal-planner')
def meal_planner():
    return "<h1>Meal Planner</h1>"

@app.route('/local-details')
def local_details():
    return "<h1>Local Details and Tips</h1>"

if __name__ == '__main__':
    app.run(debug=True)
