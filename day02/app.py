from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#127.0.0.1:5000/ssafy 주소입력했을 때
@app.route('/ssafy')
def ssafy():
    return "서버 안꺼도 됨 !!"










if __name__ == '__main__':
    app.run(debug=True)