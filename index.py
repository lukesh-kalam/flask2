from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'I am Lukesh Kumar Kalam   \n   how are you doing guys'

if __name__ == '__main__':
    app.run(debug=True)
