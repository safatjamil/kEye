import os
import sys
import subprocess
import warnings

import controller
import argparse

warnings.filterwarnings("ignore")
sys.tracebacklimit=0

required_arguements = ["service"]
handler = controller.Handler()

# parse arguements
parser = argparse.ArgumentParser()
for arg in ["-service"]:
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

status = os.popen(f"systemctl status {args.service}").read()
lines = status.split("\n")
if len(lines)<2:
    handler.response({"message": f"{status}"})
    sys.exit(1)
handler.response({"message": f"{lines[2]}"})
sys.exit(0)

