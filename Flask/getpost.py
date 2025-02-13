from flask import Flask,render_template, request

app=Flask(__name__)

@app.route("/")
def Home():
    return "Welcome to Home Page"

@app.route("/form",methods=["GET","POST"])
def Form():
    if request.method=="POST":
        name=request.form["name"]
        return f"Hello {name}"
    else:
        return render_template("form.html")




if __name__=="__main__":
    app.run(debug=True)