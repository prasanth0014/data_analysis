from flask import Flask,render_template

'''
It creates an instance of the Flask class,which will be your WSGI(Web Server Gateway Interface) application.'''

app=Flask(__name__)

@app.route("/")
def Home():
    return "Welcome to Home Page."

@app.route("/index")
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)