from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Render the sanitized demo page
    return render_template("index.html")

if __name__ == "__main__":
    # Development server - not for production use
    app.run(host="0.0.0.0", port=5000, debug=True)