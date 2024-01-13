import os
import sys
import resources
import requests
import socket
import urllib.request

# try:
#     req = requests.get(f"https://localhost:443", verify=False)
#     print(r.status)
# except:
#     print("failed")

# req = requests.get(f"https://localhost:443", verify=False)
# print(req)

var = os.popen("systemctl status apache2").read()
print(var)
lines = var.split("\n")
counter = 1
for line in lines:
    print(f"line {counter} : {line}")
    counter += 1

import yaml
with open ("/home/shafatjamil/Music/kEye/conf/api.yml", "r") as f:
    api_conf = yaml.safe_load(f)
print(api_conf)
print(type(api_conf["authentication"]))
