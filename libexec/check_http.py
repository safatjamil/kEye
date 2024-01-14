import os
import sys
import urllib.request
import requests
import warnings

import controller
import argparse

warnings.filterwarnings("ignore")
sys.tracebacklimit=0

required_arguements = ["host","port"]
protocol = "http"
handler = controller.Handler()

# parse arguements
parser = argparse.ArgumentParser()
for arg in ["-host", "-port"]:
    parser.add_argument(arg)
parser.add_argument("-secure", action="store_true")
try:
    args = parser.parse_args() 
except Exception as e:
    handler.response({"message": f"Error: {e}"})
    sys.exit(1)
for req_arg in required_arguements:
    if not getattr(args, req_arg):
        handler.response({"message": f"Required arguement(s) missing, {req_arg}"})
        sys.exit(1)
# validate the port number
try:
    p = int(args.port)
except:
    handler.response({"message": f"Port {args.port} is not valid"})
    sys.exit(1)
if getattr(args, "secure"):
    protocol = "https"

try:
    req = requests.get(f"{protocol}://{args.host}:{args.port}", verify=False, timeout=10)
    if req.status_code == 200:
        handler.response({"message": f"{protocol}-OK, response code: 200"})
        sys.exit(0)
    else:
        handler.response({"message": f"{protocol}-ERROR, response code: {req.status_code}"})
        sys.exit(1)
except:
    handler.response({"message": f"Can not connect to {args.host} on port {args.port}"})
    sys.exit(1)
    
    


