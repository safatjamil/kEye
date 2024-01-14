import yaml
from main import filehandler, resources


class Api:
    
    def __init__(self, file):
        self.file = file
        self.service_resource = resources.ServiceResource()
        self.dir_resource = resources.DirResource()
        self.file_handler = filehandler.FileHandler()
    
    def validate(self):
        return_ = {"message": "", "error": ""}
        try:
            with open(f"{self.file}", "r") as f:
                api_conf = yaml.safe_load(f)
            if ("authentication" not in api_conf or
                type(api_conf["authentication"]) != bool):
                return_["status"] = False
                return_["error"] = "Please add boolean value in the authentication field"
                return return_
            for key in api_conf.keys():
                if key == "authentication":
                    continue
                if "password" not in api_conf[key]:
                    return_["status"] = False
                    return_["error"] = f"Please provide password for the user {key}"
                    return return_
                if not api_conf[key]["password"] or len(api_conf[key]["password"])<6:
                    return_["status"] = False
                    return_["error"] = f"Password would be at least 6 characters long for the user {key}"
                    return return_
            return_["status"] = True
            return_["message"] = "Api configuration is valid"
            return return_
        except Exception as e:
            return_["status"] = False
            return_["message"] = "Something went wrong"
            return_["error"] = e
            return return_
        
    def generate(self):
        try:
            with open(f"{self.file}", "r") as f:
                api_conf = yaml.safe_load(f)
            return api_conf
        except Exception as e:
            return None

    def is_auth_enabled(self):
        return_ = {"message": "", "error": ""}
        try:
            with open(f"{self.file}", "r") as f:
                api_conf = yaml.safe_load(f)
            if ("authentication" not in api_conf or
                type(api_conf["authentication"]) != bool):
                return_["status"] = False
                return_["error"] = "Please add boolean value in the authentication field"
                return return_
            if api_conf["authentication"] == True:
                return_["status"] = True
                return_["authentication"] = True
                return_["message"] = ""
                return return_
            else:
                return_["status"] = True
                return_["authentication"] = False
                return return_
        except Exception as e:
            return_["status"] = False
            return_["message"] = "Something went wrong"
            return_["error"] = e
            return return_

    def authenticate_user(self, user, password):
        return_ = {"status": True, "message": "", "error": ""}
        try:
            with open(f"{self.file}", "r") as f:
                api_conf = yaml.safe_load(f)
            if user not in api_conf:
                return_["auth"] = False
                return_["message"] = "Api user not found"
                return return_
            if api_conf[user]["password"] != password:
                return_["auth"] = False
                return_["message"] = f"Password is not correct for this api user {user}"
                return return_
            return_["auth"] = True
            return_["message"] = "User authentication successful"
            return return_
        except Exception as e:
            return_["status"] = False
            return_["error"] = e
            return return_


