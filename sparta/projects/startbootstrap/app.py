from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def dashboard():
    return render_template('index.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/blank.html')
def blank():
    return render_template('blank.html')

@app.route('/buttons.html')
def buttons():
    return render_template('buttons.html')

@app.route('/cards.html')
def cards():
    return render_template('cards.html')

@app.route('/charts.html')
def charts():
    return render_template('charts.html')

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/tables.html')
def tables():
    return render_template('tables.html')

@app.route('/utilities-animation.html')
def animation():
    return render_template('utilities-animation.html')

@app.route('/utilities-border.html')
def border():
    return render_template('utilities-border.html')

@app.route('/utilities-color.html')
def color():
    return render_template('utilities-color.html')

@app.route('/utilities-other.html')
def other():
    return render_template('utilities-other.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)