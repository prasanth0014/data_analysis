#dynamic urls
from flask import Flask, render_template,redirect,url_for

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return "Welcome to Home Page Nanba."
#variable
@app.route("/index/<val>")
def index(val):
    return "you entered "+val
#jinj2 template
'''
used to write python code in html file:
{{}}->used to access variable value
{%%}->writing for if
{##}->comments
'''

#request particular datatype
@app.route("/index1/<int:val>")
def index1(val):
    return "you entered "+str(val)

@app.route("/index2/<int:val>")
def index2(val):
    return render_template("dynamic.html",val=val)

dict={"a":10,"b":20}
@app.route("/index3/<int:val>")
def index3(val):
    return render_template("dynamic.html",dict=dict,val=val)

#how to build dynamic urls i.e call another url from one url
@app.route("/index4")
def index4():
    val=50
    return redirect(url_for("index3",val=val))
if __name__ == "__main__":
    app.run(debug=True)
