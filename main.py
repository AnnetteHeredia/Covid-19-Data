from flask import Flask, render_template
import flask
app = Flask(__name__)
@app.route('/')
def home():
    print(flask.current_app.root_path)
    return "Hello"
    # return render_template('Project\ 3\ Home/index.html')

if __name__ == "__main__":
    app.run(debug=True)
    