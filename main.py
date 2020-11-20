from flask import send_from_directory,Flask,session
import os
import datetime
import conf
app = Flask(__name__,static_folder="{}/static".format(conf.reactBuildPath))
app.secret_key = conf.flaskSecret

@app.route('/', defaults={'upath': ''})
@app.route('/<path:upath>')
def serve(upath):
    sessionManager(session)
    path_dir = "{}".format(conf.reactBuildPath)
    if upath != "" and os.path.exists(os.path.join(path_dir, upath)):
        return send_from_directory(os.path.join(path_dir), upath)
    else:
        return send_from_directory(os.path.join(path_dir),'index.html')

def sessionManager(session:session):
    try:
        print(session["uid"])
    except KeyError:
        session["uid"] = str(datetime.datetime.now())

app.run(conf.serverIp,conf.serverPort,conf.debug)