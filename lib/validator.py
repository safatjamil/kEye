import sys
import os
import argparse
import toml
import yaml

import service
import resources
import filehandler
import api

sys.tracebacklimit=0
file_handler = filehandler.FileHandler()
service_resource = resources.ServiceResource()
conf_resource = resources.ConfResource()

# parse arguements
parser = argparse.ArgumentParser()
parser.add_argument("-dry-run", action="store_true")
try:
    args = parser.parse_args() 
except Exception as e:
    handler.response({"message": f"Error: {e}"})
    sys.exit(1)

# validate services.toml
# check if file exists
if not file_handler.check_file_exists(conf_resource.service_conf_file):
   sys.exit(f"Error: {conf_resource.service_conf_file} file doesn't exist")
# check file permission
if not file_handler.check_permission(conf_resource.service_conf_file, "r"):
   sys.exit(f"Error: Check the permission of {conf_resource.service_conf_file}")
service_ = service.Service(conf_resource.service_conf_file)
response = service_.validate()
services = service_.generate()
if not response["status"]:
   print(response["error"])
   sys.exit(1)
print(response)

# validate api.yml
# check if file exists
if not file_handler.check_file_exists(conf_resource.api_conf_file):
   sys.exit(f"Error: {conf_resource.api_conf_file} file doesn't exist")
# check file permission
if not file_handler.check_permission(conf_resource.api_conf_file, "r"):
   sys.exit(f"Error: Check the permission of {conf_resource.api_conf_file}")
api_ = api.Api(conf_resource.api_conf_file)
response = api_.validate()
if not response["status"]:
   print(response["error"])
   sys.exit(1)
print(response)



         
    
    





