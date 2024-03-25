# app entry point
# from app import create_app

# app = create_app()

from flask import Flask
app = Flask(__name__)

@app.route('/')
def test():
    return 'test'


if __name__ == "__main__":
    app.run(debug=True)