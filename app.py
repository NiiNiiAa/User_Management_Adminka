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

@app.errorhandler(403)
def error_403(e):
    return render_template("/errors/403.html"), 403

@app.errorhandler(404)
def error_404(e):
    return render_template("/errors/404.html"), 404

@app.errorhandler(500)
def error_500(e):
    return render_template("/errors/500.html"), 500

if __name__ == "__main__":
    app.run(debug=True)