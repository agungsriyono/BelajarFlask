from flask import Flask
app = Flask(__name__)

# @app.route('/')


@app.route('/hello')
def hello_world():
    return "Hello World"


app.add_url_rule('/', 'hello', hello_world)

# if __name__ == '__main__':
#     app.debug = True
#     app.run()
#     # app.run(debug = True)
#     # app.run()

app = Flask(__name__)


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name


if __name__ == '__main__':
    app.run(debug=True)
