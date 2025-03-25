from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/auth")
def auth():
    return render_template("auth.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/about")
def contact():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)