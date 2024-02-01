from flask import Flask, send_from_directory, logging
import os
#import logging
from waitress import serve
from paste.translogger import TransLogger

app = Flask(__name__)
#app.logger.setLevel(logging.INFO)
#logging.basicConfig()
#logging.getLogger().setLevel(logging.INFO)
@app.route("/")
def tos():
    workingdir = os.path.abspath(os.getcwd())
    return send_from_directory(workingdir, 'resume_OscarIvanSanchezAmaya.pdf')

if __name__ == "__main__":
    serve(TransLogger(app), host="0.0.0.0", port=80)