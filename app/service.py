import toml
import resources
import filehandler


class Service:
    def __init__(self, file):
        self.file = file
        self.serv_dicts = {} 
        self.return_ = {}
        self.service_resource = resources.ServiceResource()
        self.dir_resource = resources.DirResource()
        self.file_handler = filehandler.FileHandler()
        
    def validate(self):
        with open(self.file, "r") as f:
            try:
                services = toml.load(f)
                required_attributes = self.service_resource.hierarchy["service"]["required"]
                optional_attributes = self.service_resource.hierarchy["service"]["optional"]
                self.serv_dicts = {}
                for service in services.keys():
                    self.serv_dicts[service] = {}
                    # get all the required attributes
                    tmp_required_attributes = list(self.service_resource.hierarchy["service"]["required"].keys())
                    found = set()
                    for key in services[service].keys():
                        # check valid attribute
                        if (key not in required_attributes and
                            key not in optional_attributes):
                            self.return_["status"] = False
                            self.return_["error"] = f"{key},invalid attribute of {service}" 
                            return self.return_
                        # append the required attributes to a found list
                        if (key in required_attributes and 
                            key not in found):
                            found.add(key)
                            tmp_required_attributes.remove(key)
                        # check attribute type
                        if (key in required_attributes or 
                            key in optional_attributes):
                            if type(services[service][key]) != required_attributes[key]["type"]:
                                self.return_["status"] = False
                                self.return_["error"] = f"{key},invalid attribute type of {service}. Valid type should be {required_attributes[key]['type']}" 
                                return self.return_
                            if key == "check_script":
                                commands = services[service][key].split("!")
                                if not self.file_handler.check_file_exists(f"{self.dir_resource.package_dir}/libexec/{commands[0]}"):
                                    self.return_["status"] = False
                                    self.return_["error"] = f"missing check script for {service}. File {services[service][key]} is not found at {self.dir_resource.package_dir}/libexec/"
                                    return self.return_
                                self.serv_dicts[service]["check_script"] = f"{self.dir_resource.package_dir}/libexec/{commands[0]}"
                                self.serv_dicts[service]["args"] = [commands[i] for i in range(1,len(commands))]
                                continue
                            self.serv_dicts[service][key] = services[service][key]

                    if len(found) < len(required_attributes):
                        self.return_["status"] = False
                        self.return_["error"] = "missing attribute(s) "+ ",".join(tmp_required_attributes)+ " for "+ service
                        return self.return_
                self.return_["status"] = True
                self.return_["message"] = "Service configuration is valid"
                return self.return_

            except Exception as e:
                self.return_["action"] = False
                self.return_["error"] = e
                return self.return_
       
    def generate(self):
        return self.serv_dicts