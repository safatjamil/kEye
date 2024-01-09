import os
class FileHandler:

    def check_extension(self, extension, file):
        if len(file) < len(extension) or (file[-len(extension):-1]+file[-1]) != extension:
            return False
        return True
    
    def check_file_exists(self, file):
        if os.path.isfile(file):
            return True
        return False
    
    def check_permission(self, file, mode):
        try:
            f = open(file, mode)
            return True
        except:
            return False

    
        