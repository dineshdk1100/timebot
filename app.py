from flask import Flask,jsonify
import time


app= Flask(__name__)

@app.route('/api')
def apiFunc():
    d=dict()
    d['result'] = "working"
    d['time']=time.asctime(time.localtime(time.time()))
    # print(currtime)
    return jsonify(d)


if __name__ == '__main__':
    app.run()