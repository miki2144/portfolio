from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

# Home Route
@app.route('/')
def home():
    return render_template('home.html')

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# Experience Route
@app.route('/experience')
def experience():
    return render_template('experience.html')

# Skills Route
@app.route('/skills')
def skills():
    return render_template('skills.html')

# Contact Route
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
