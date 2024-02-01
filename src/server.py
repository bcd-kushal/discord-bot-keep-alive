import flask 
from threading import Thread



# ==[ FLASK CODE ]===========================================================

app = flask.Flask('')


@app.route('/', methods=['GET'])
def keep_running():
    if flask.request.method == "GET":
        return flask.jsonify({ "status": "success", "data": "successfully called this API." }), 200
    else:
        return flask.jsonify({ "status": "failure", "data": "only GET requests supported" }), 405


def server():
    app.run( host='0.0.0.0' )

def run_server():
    t = Thread(target=server)
    t.start()