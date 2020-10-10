from flask import Flask, request
from challenges import fibd
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello!'



@app.route('/fibd')
def mortal_fibonacci_rabbits():
    n = request.args.get('n', 6)
    m = request.args.get('m', 4)
    ans = fibd.mortal_fib_rabbits(int(n), int(m))
    return str(ans)