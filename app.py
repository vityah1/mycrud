import os, sys

import codecs
from flask import (
    Flask,
    request,
)

from api import ajax_bp

app = Flask(__name__)

app.register_blueprint(ajax_bp)


def __repr__(self):
    return "<Mysession %r" % self.id


@app.route("/")
# @check_ip()
def info():
    root_dir = os.path.dirname(os.getcwd())
    app_root_path = app.root_path
    return {
        "ip": f"{request.remote_addr}",
        "root dir": f"{root_dir}",
        "app_root_path": f"{app_root_path}",
        "os_name": f"{os.name}",
    }


@app.errorhandler(404)
def page_not_found(error):
    return {"status": "error", "data": "page not found"}, 404


if __name__ == "__main__":
    #    app.run(debug=True)
    #    app.debug=True
    #    app.run(host='0.0.0.0',port=4000)
    #    app.run(host='0.0.0.0',port=80,debug=False)
    app.run(host="0.0.0.0", port=5000, debug=True)
