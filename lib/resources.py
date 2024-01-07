import sys
import os
# append the parent directory to the sys path
sys.path.append(os.getcwd()[:-4])


class DirResource:
    package_dir = os.getcwd()[:-4]

class ConfResource:
    
    service_conf_file = sys.path[-1] + "/conf/services.toml"
    api_conf_file = sys.path[-1] + "/conf/api.yml"

class ServiceResource:

    file_properties = {"extenxion": ".toml"}
    hierarchy = {"service":{"required":{"check_script":{"required":{}, "optional":{},"type":str}},
                            "optional": {},
                            "type": str
                            }
                }
