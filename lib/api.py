import yaml
import resources
import filehandler


class Api:
    
    def __init__(self, file):
        self.file = file
        self.api_dicts = {} 
        self.return_ = {}
        self.service_resource = resources.ServiceResource()
        self.dir_resource = resources.DirResource()
        self.file_handler = filehandler.FileHandler()
    
    def validate(self):
        try:
            with open(f"{self.file}", "r") as f:
                api_conf = yaml.safe_load(f)
            if ("authentication" not in api_conf or
                type(api_conf["authentication"]) != bool):
                self.return_["status"] = False
                self.return_["error"] = "Please add boolean value in the authentication field"
                return self.return_
            for key in api_conf.keys():
                if key == "authentication":
                    continue
                if "password" not in api_conf[key]:
                    self.return_["status"] = False
                    self.return_["error"] = f"Please provide password for the user {key}"
                    return self.return_
                if not api_conf[key]["password"] or len(api_conf[key]["password"])<6:
                    self.return_["status"] = False
                    self.return_["error"] = f"Password would be at least 6 characters long for the user {key}"
                    return self.return_
            self.return_["status"] = True
            self.return_["message"] = "Api configuration is valid"
            return self.return_
        except Exception as e:
            self.return_["status"] = False
            self.return_["error"] = e
            return self.return_
        
        