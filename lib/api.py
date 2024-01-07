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
            self.return_["status"] = True
            self.return_["api_conf"] = api_conf
            return self.return_
        except Exception as e:
            self.return_["status"] = False
            self.return_["message"] = e
            return self.return_
        
        