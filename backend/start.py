from flask import Flask

app = Flask(__name__) #记住这里的变量名app

@app.route('/')
def hello():
    return 'hello docker&flask'

if __name__ == '__main__':
    app.run(debug=True)