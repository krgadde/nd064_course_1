import json
from flask import Flask
from flask import Response
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("Main request successfull")
    return "Hello World!"

@app.route("/status")
def httpstatus():
    response= app.response_class(response=json.dumps({'result':'OK - healthy'}),status=200,mimetype='application/json')
    app.logger.info("Status request successfull")
    return response
    #status_code = flask.Response(status=200)
    #return status_code
    #return Response("{'result':'OK - healthy'}", status=status_code, mimetype='application/json')


@app.route("/metrics")
def appmetrics():
    app.logger.info("Metrics request successfull")
    return Response("{'UserCount':'140','UserCountActive':'23'}", status=200, mimetype='application/json')

if __name__ == "__main__":
    logging.basicConfig(filename="app.log",level=logging.DEBUG)
    app.run(host='0.0.0.0')
