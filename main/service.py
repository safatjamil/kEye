import toml
from main import filehandler, resources


class Service:
    def __init__(self, file):
        self.file = file
        self.service_resource = resources.ServiceResource()
        self.dir_resource = resources.DirResource()
        self.file_handler = filehandler.FileHandler()
        
    def validate(self):
        return_ = {"message": "", "error": ""}
        try:
            with open(self.file, "r") as f:
                services = toml.load(f)
            required_attributes = self.service_resource.hierarchy["service"]["required"]
            optional_attributes = self.service_resource.hierarchy["service"]["optional"]
            for service in services.keys():
                # get all the required attributes
                tmp_required_attributes = list(self.service_resource.hierarchy["service"]["required"].keys())
                found = set()
                for key in services[service].keys():
                    # check valid attribute
                    if (key not in required_attributes and
                        key not in optional_attributes):
                        return_["status"] = False
                        return_["error"] = f"{key},invalid attribute of {service}" 
                        return return_
                    # append the required attributes to a found list
                    if (key in required_attributes and 
                        key not in found):
                        found.add(key)
                        tmp_required_attributes.remove(key)
                    # check attribute type
                    if (key in required_attributes or 
                        key in optional_attributes):
                        if type(services[service][key]) != required_attributes[key]["type"]:
                            return_["status"] = False
                            return_["error"] = f"{key},invalid attribute type of {service}. Valid type should be {required_attributes[key]['type']}" 
                            return return_
                        if key == "check_script":
                            commands = services[service][key].split("!")
                            if not self.file_handler.check_file_exists(f"{self.dir_resource.package_dir}/libexec/{commands[0]}"):
                                return_["status"] = False
                                return_["error"] = f"missing check script for {service}. File {services[service][key]} is not found at {self.dir_resource.package_dir}/libexec/"
                                return return_
                if len(found) < len(required_attributes):
                    return_["status"] = False
                    return_["error"] = "missing attribute(s) "+ ",".join(tmp_required_attributes)+ " for "+ service
                    return return_
            return_["status"] = True
            return_["message"] = "Service configuration is valid"
            return return_

        except Exception as e:
            return_["status"] = False
            return_["message"] = "Something went wrong"
            return_["error"] = e
            return return_
    
    def generate(self):
        try:
            with open(f"{self.file}", "r") as f:
                service_conf = yaml.safe_load(f)
            return service_conf
        except Exception as e:
            return None
    
    def get_service(self, service):
        return_ = {"message": "", "error": ""}
        try:
            with open(self.file, "r") as f:
                services = toml.load(f)
            if service not in services.keys():
                return_["status"] = False
                return_["message"] = "Service not found"
                return return_
            return_["status"] = True
            return_["data"] = services[service]
            return return_
        except Exception as e:
            return_["status"] = False
            return_["message"] = "Something went wrong"
            return_["error"] = e
            return return_
