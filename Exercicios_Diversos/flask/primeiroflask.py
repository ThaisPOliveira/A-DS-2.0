from flask import Flask, redirect, url_for
app=Flask(__name__)
@app.route("/")
def home():
    return "Hello world<h2>TITULO</h2>"
@app.route("/<name>")
def user(name):
    return f"OLa {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("user"))
if __name__ == "__main__":
    app.run()