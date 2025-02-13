from doctest import debug
from flask import Flask,render_template,redirect,url_for,request

app=Flask(__name__)

items=[
    {"id":1,"name":"prasanth","desc":"need to study html"}

]
@app.route("/")
def Home():
    return "Welcome to Home Page"

@app.route("/list",methods=["GET"])
def List():
    if not items:
        return {"name":"error","desc":"list not occur"}
    else :
        return items

@app.route("/add",methods=["POST"])
def add():
    if request.json:
        item={}
        item["id"]=items[-1]["id"]+1  if len(items) >=1 else 1
        item["name"]=request.json["name"]
        item["desc"]=request.json["desc"]
        items.append(item)
        return items
    else:
        return {"name":"error","desc":"list not occur"}
    
@app.route("/update",methods=["PUT"])
def update():
    item=[item for item in items if item["id"]==request.json["id"]]
    item=item[0]
    item["name"]=request.json.get("name",item["name"])
    item["desc"]=request.json.get("desc",item["desc"])
    for i in range(len(items)):
        if item["id"]==items[i]["id"]:
            items[i]=item
            break
    return item

@app.route("/delete/<id>",methods=["DELETE"])
def delete(id):
    global items
    items=[item for item in items if item["id"]!=id]
    return items

if __name__=="__main__":
    app.run(debug=True)
