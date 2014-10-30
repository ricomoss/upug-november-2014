from flask import Flask, request
app = Flask(__name__)


def fib(n):
    if n < 2:
        return 0
    a = 0
    b = 1
    i = 0
    while i < n:
        c = a + b
        a = b
        b = c
        i += 1
    return b


@app.route('/fib-num/', methods=['GET'])
def fib_num():
    if request.method == 'GET':
        return str(fib(int(request.args.get('num', 0))))
    else:
        return 'Incorrect request type {}'.format(request.method)


if __name__ == '__main__':
    app.run()
