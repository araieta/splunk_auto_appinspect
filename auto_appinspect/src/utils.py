import configparser



def _read_config(config_file_path):
    
    config = configparser.ConfigParser()
    config.read(config_file_path)
    return config

def get_credentials(config_file_path):

    rconf = _read_config(config_file_path)
    username = rconf.get('Credentials', 'username')
    password = rconf.get('Credentials', 'password') 
    return username, password


def get_path(config_file_path):
    
    rconf = _read_config(config_file_path)
    return rconf.get('Path', 'app')

def get_path_report(config_file_path):
    
    rconf = _read_config(config_file_path)
    return rconf.get('Path', 'report')
    
    
def create_folders():
    import os
    
    directories = ["log","HTML_reports"]
    parent = ""

    for dir in directories:
            
        path = os.path.join(parent, dir)
        if not os.path.isdir(path):
            
            os.makedirs(path)
            print(f"Created Folders {dir}")
        else:
            print("Folders Exists!")
        