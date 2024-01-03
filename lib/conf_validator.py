import sys
import os
import argparse
import toml
import service
import resources
import filehandler
import service

sys.tracebacklimit=0

#get the file
try:
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", required=True)
    args = parser.parse_args() 
    conf_file = args.c
except:
   sys.exit(1)


file_handler = filehandler.FileHandler()
service_resource = resources.ServiceResource()
conf_resource = resources.ConfResource()

# check it is the correct conf file
if args.c != conf_resource.service_conf_file:
   raise Exception(f"Error: The service configuration file should be {conf_resource.service_conf_file}")
   sys.exit(1)

# check if file exists
if not file_handler.check_file_exists(args.c):
   sys.exit(f"Error: {conf_file} file doesn't exist")

# check file permission
if not file_handler.check_permission(conf_file, "r"):
   sys.exit(f"Error: Check the permission of {conf_file}")

service = service.Service(conf_file)
response = service.validate()
print(response)


         
    
    





