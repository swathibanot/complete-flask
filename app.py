from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello():
    return '<h1>Hello,World!</h1>'

@app.route('/about',methods=['GET'])
def about():
    return '<h1>About our company</h1>'

if __name__ =='__main__':
    app.run(debug=True)