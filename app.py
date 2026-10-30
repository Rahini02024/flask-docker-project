from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to My Flask Application!</h1>
    <p>My first Docker project is running successfully.</p>
    <p>Created by Rahini R</p>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
