from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('statement.html')

@app.route('/tricare')
def tricare():
    return "<h1>Tricare</h1>"

@app.route('/commissary')
def commissary():
    return "<h1>Commissary</h1>"

@app.route('/mpf')
def mpf():
    return "<h1>MPF</h1>"

@app.route('/itt')
def itt():
    return "<h1>ITT</h1>"

@app.route('/local-details')
def local_details():
    return "<h1>Local Details and Tips</h1>"

if __name__ == '__main__':
    app.run(debug=True)
