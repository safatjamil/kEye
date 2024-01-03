import toml
import resources
import filehandler

class Service:
    
    def __init__(self, file):
        self.file = file
        # default attributes
        self.services = []
        self.line_count = 0
        self.data = {}
        self.error = ""
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
                
                for service in services.keys():
                    # get all the required attributes
                    tmp_required_attributes = list(self.service_resource.hierarchy["service"]["required"].keys())
                    found = set()
                    for key in services[service].keys():
                        # check valid attribute
                        if key not in required_attributes and key not in optional_attributes:
                            self.return_["status"] = False
                            self.return_["error"] = f"Error: {key},invalid attribute of {service}" 
                            return self.return_
                        # check attribute type
                        if key in required_attributes or key in optional_attributes:
                            if type(services[service][key]) != required_attributes[key]["type"]:
                                self.return_["status"] = False
                                self.return_["error"] = f"Error: {key},invalid attribute type of {service}. Valid type should be {required_attributes[key]['type']}" 
                                return self.return_
                            if (key == "check_script" 
                                and not self.file_handler.check_file_exists(self.dir_resource.package_dir)):
                                self.return_["status"] = False
                                self.return_["error"] = f"Error: {services[service][key]}, missing check script for {service}. File is not found at {self.dir_resource.package_dir}/check_scripts/"
                                return self.return_
                        # append the required attributes to a found list
                        if key in required_attributes and key not in found:
                            found.add(key)
                            tmp_required_attributes.remove(key)
                    if len(found) < len(required_attributes):
                        self.return_["status"] = False
                        self.return_["error"] = "Error: missing attribute(s) " + ",".join(tmp_required_attributes)+ " for " + service
                        return self.return_
                self.return_["status"] = True
                self.return_["message"] = "Service parsing is successful"

            except Exception as e:
                self.return_["action"] = False
                self.return_["error"] = e #e.lineno + e.msg
                return self.return_
       