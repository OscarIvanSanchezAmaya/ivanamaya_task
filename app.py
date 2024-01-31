from flask import Flask, send_from_directory
import os
from waitress import serve

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
@app.route("/")
def tos():
    workingdir = os.path.abspath(os.getcwd())
    return send_from_directory(workingdir, 'resume_OscarIvanSanchezAmaya.pdf')

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=80)