import requests


def auth(username, password):
    
    url = 'https://api.splunk.com/2.0/rest/login/splunk'
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        print("Autenticato con successo")
        return response.json()
    
    
def get_token(data):
    return data["data"]['token']

def validate_app_package(token, file_path):
    
    url = "https://appinspect.splunk.com/v1/app/validate"
    
    headers = { "Authorization": f"Bearer {token}" }
    
    files = { 'app_package': (file_path, open(file_path, 'rb')) }

    try:
        print("Caricamento In Corso....")
        response = requests.post(url, headers=headers, files=files)
        print("Ok...")
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Stack Trace Error --> {e}")
        

def get_request_id(data):
    return data['request_id']
    
def status(token, request_id):
    # URL dell'endpoint
    url = f"https://appinspect.splunk.com/v1/app/validate/status/{request_id}"
    
    # Header della richiesta
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Stack Trace Error --> {e}")

        
def get_app_report(token, request_id):
    # URL dell'endpoint
    url = f"https://appinspect.splunk.com/v1/app/report/{request_id}"
    
    # Header della richiesta
    headers = {
        "Authorization": f"Bearer {token}",
        "Cache-Control": "no-cache",
        "Content-Type": "text/html"
    }
    
    try:
        response = requests.get(url, headers=headers)
        return response.text
    
    except requests.exceptions.RequestException as e:
        print(f"Stack Trace Error --> {e}")