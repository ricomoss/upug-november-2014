from flask import Flask, request
app = Flask(__name__)


def fib(n):
    if n < 1:
        return 0
    if n < 3:
        return 1
    a = 0
    b = 1
    i = 0
    while i < n - 1:
        c = a + b
        a = b
        b = c
        i += 1
    return b


@app.route('/fib-num/', methods=['GET'])
def fib_num():
    if request.method == 'GET':
        return str(fib(int(request.args.get('fib_index', 0))))
    else:
        return 'Incorrect request type {}'.format(request.method)


if __name__ == '__main__':
    app.run()
