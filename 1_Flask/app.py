from flask import Flask, request

app = Flask(__name__)


# @app.route('/')
# def hello():
#     return 'Hello!'

@app.route('/request')
def request_info():
    return 'request method: {0} url: {1} headers: {2}'.format(
        request.method, request.url, request.headers
    )


if __name__ == '__main__':
    app.run(debug=True)