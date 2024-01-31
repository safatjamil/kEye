import sys
import os
import subprocess
from flask import Flask,jsonify,request

import conf
import libexec
from main import api, filehandler, resources, service
app = Flask(__name__)
api_conf = f"{os.getcwd()}/conf/api.yml"
service_conf = f"{os.getcwd()}/conf/services.toml"
api_ = api.Api(api_conf)
service_ = service.Service(service_conf)

@app.route('/api/<service>/status/', methods = ['GET'])
def service_status(service):
    data = request.get_json()
    response = {}
    api_auth = api_.is_auth_enabled()
    if api_auth["status"] == False:
        response["message"] = api_auth["error"]
        return jsonify(response), 200
    if api_auth["status"] == True:
        if ("username" not in data or
           "password" not in data):
            response["message"] = "Please provide your api username and password"
            return jsonify(response), 401
        user_auth = api_.authenticate_user(data["username"], data["password"])
        if user_auth["status"] == False:
            response["message"] = "Something went wrong"
            return jsonify(response), 500
        if user_auth["auth"] == False:
            response["message"] = user_auth["message"]
            return jsonify(response), 401

    service_det = service_.get_service(service)
    if service_det["status"] == False:
        response["message"] = service_det["message"]
        return jsonify(response), 400

    commands = service_det["data"]["check_script"].split("!")
    commands[0] = "libexec/" + commands[0]
    # fetch the executable path
    with open(commands[0], "r") as f:
        lines = f.readlines()
    exec_ = lines[0][2:]
    exec_ = exec_.replace("\n", "")
    commands = [exec_] + commands
    output = subprocess.run(commands, capture_output=True)
    response_code = 200
    response["status"] = output.stdout.decode().replace("\n", "").strip()
    if output.returncode != 0:
        response_code = 503
    return jsonify(response), response_code
 
if __name__ == '__main__':
    app.run(debug=True)
