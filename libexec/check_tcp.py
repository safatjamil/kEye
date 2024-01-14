import os
import sys
import socket
import warnings

import controller
import argparse

warnings.filterwarnings("ignore")
sys.tracebacklimit=0

required_arguements = ["host","port"]
handler = controller.Handler()

# parse arguements
parser = argparse.ArgumentParser()
for arg in ["-host", "-port"]:
    parser.add_argument(arg)
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
# create a tcp socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)
try:
    s.connect((args.host, int(args.port)))
    handler.response({"message": f"Tcp-ok to {args.host} on port {args.port}"})
    s.close()
    sys.exit(0)
except Exception as e:
    handler.response({"message": f"Can not connect to {args.host} on port {args.port}. Error: {e}"})
    s.close()
    sys.exit(1)

     
    


