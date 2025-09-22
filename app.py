from flask import Flask,render_template

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def  login():
    return render_template('login.html')

@app.route('/seccee')
def red():
    return render_template('seccee.html')
@app.route('/sigging')
def sigging():
    return render_template('sigging.html')

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True) # debug=True enables auto-reloading and a debugger