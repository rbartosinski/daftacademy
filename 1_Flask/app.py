import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'


@app.route('/method', methods=['GET', 'POST', 'PUT', 'DELETE'])
def method_info():
    return '{0}'.format(request.method)


@app.route('/show_data', methods=['POST'])
def show_data():
    data = request.data
    #data = request.get_json()
    #return '{0}'.format(data2)
    return data


@app.route('/pretty_print_name', methods=['POST'])
def print_name():
    data = request.get_json()
    name = data["name"]
    surename = data["surename"]
    return 'Na imię mu {0}, a nazwisko jego {1}'.format(name, surename)


counter_value = 0


@app.route('/counter')
def counter():
    global counter_value
    if request:
        counter_value += 1
    return '{0}'.format(counter_value)


@app.route('/request')
def request_info():
    return 'request method: {0} url: {1} headers: {2}'.format(
        request.method, request.url, request.headers
    )


if __name__ == '__main__':
    app.run(debug=True)