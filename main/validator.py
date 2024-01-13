import sys
import os
import argparse
import toml
import yaml

sys.path.append(os.getcwd())
from main import api, filehandler, resources, service

sys.tracebacklimit=0
file_handler = filehandler.FileHandler()
service_resource = resources.ServiceResource()
dir_ = os.getcwd()
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
conf_file = f"{os.getcwd()}/conf/services.toml"
if not file_handler.check_file_exists(f"{conf_file}"):
   print(f"Error: {conf_file} file doesn't exist")
   sys.exit(1)
# check file permission
if not file_handler.check_permission(conf_file, "r"):
   print(f"Error: Check the permission of {conf_file}")
   sys.exit(1)
service_ = service.Service(conf_file)
response = service_.validate()
if not response["status"]:
   print(f'Error: {response["error"]}. Check {conf_file}')
   sys.exit(1)
print(f'{response["message"]}')

# validate api.yml
# check if file exists
api_conf = f"{os.getcwd()}/conf/api.yml"
if not file_handler.check_file_exists(api_conf):
   print(f"Error: {api_conf} file doesn't exist")
   sys.exit(1)
# check file permission
if not file_handler.check_permission(api_conf, "r"):
   print(f"Error: Check the permission of {api_conf}")
   sys.exit(1)
api_ = api.Api(api_conf)
response = api_.validate()
if not response["status"]:
   print(f'Error: {response["error"]} in {api_conf}')
   sys.exit(1)
print(f'{response["message"]}')
sys.exit(0)






         
    
    





