from src.utils import get_credentials, get_path, get_path_report, create_folders
from src.api_appinspect import auth, get_token, validate_app_package, status, get_request_id, get_app_report
import datetime
import os, time
import logging


if __name__ == "__main__":

    print("""
          ╔═╗╔═╗╔═╗╦╔╗╔╔═╗╔═╗╔═╗╔═╗╔╦╗
          ╠═╣╠═╝╠═╝║║║║╚═╗╠═╝║╣ ║   ║ 
          ╩ ╩╩  ╩  ╩╝╚╝╚═╝╩  ╚═╝╚═╝ ╩ 
          """)
    
    create_folders()
    logger = logging.getLogger(__name__)
    logging.basicConfig(
                        filename='C:\\Users\\AndreaRaieta\\lab\\auto_appinspect\\venv\\log\\app.log', 
                        encoding='utf-8',
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.INFO,
                        filemode="a"
                        )
    
    username, password = get_credentials(".\\.config")
    path = get_path(".\\.config")
    app_name = path.split("/")[-1]
    
    data = auth(username, password)
    token_from_auth = get_token(data)
    
    path_app = path

    logging.info(f'path app ....> { path_app }')
    submit = validate_app_package(token_from_auth, path_app)
    request_id = get_request_id(submit)
    start = datetime.datetime.now().time()
    
    stat = "PROCESSING"
    logging.info(f"Start Process ----> {  start  }")
    while( stat == 'PROCESSING'):
        stat = status(token_from_auth, request_id)['status']
        print(f"Still In Processing... { datetime.datetime.now() }")
        logging.info(f"Still In Processing... { datetime.datetime.now() }")
        print(time.sleep(200))
        
        
    end = datetime.datetime.now()
    report = get_app_report(token_from_auth, request_id)
    
    dt = datetime.datetime.now().isoformat("T","seconds").replace("-","").replace(":","")
    logging.info(f"END PROCESS ----> {  dt  }")
    try:
        p = os.join.path(get_path_report('.\\.config'),"")
        with open(f"{p}_report_{dt}.html", "w") as f:
            f.write(report)
            logging.info(f"Report created in {p}")
            print("Report Created!")
    except Exception as e:
        logging.error(f"Stack Trace ----> {  e  }")