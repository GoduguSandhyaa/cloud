
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to CloudApp!</h1>
    <p>Application deployed using PaaS.</p>
    <p>Cloud Computing Week 3 Laboratory</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

