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
