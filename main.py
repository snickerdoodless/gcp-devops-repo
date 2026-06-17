from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    model = {"title":"Hello From GCP Pipeline"}
    return render_template('index.html', model=model)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int("8080"), threaded=True)