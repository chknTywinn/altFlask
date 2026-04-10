from flask import Flask, render_template, redirect,url_for , request
from tinydb import TinyDB

app = Flask(__name__, template_folder="templates1", static_folder="static1")
db = TinyDB("db/notes.json")
notes = db.all()

@app.route("/")
def index():
    notes = db.all()
    return render_template("index.html", notes=notes)

@app.route("/delete/<int:id>")
def delete(id):
    db.remove(doc_ids=[id])
    return redirect(url_for("index"))

@app.route("/edit/<int:id>")
def edit(id):
    note = db.get(doc_id=id)
    return render_template("edit.html", note=note)

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    db.update({
    "naslov": request.form["title"],
    "vsebina": request.form["content"]},
    doc_ids=[id])
    return redirect(url_for("index"))

@app.route("/add", methods=["POST"])
def add():
    db.insert({
    "naslov": request.form["title"],
    "vsebina": request.form["content"]})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)