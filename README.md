# splunk_auto_appinspect  

![Logo](/static/wwo.png)

A script in python to automate your splunk app check with app inspect Splunk API

## Configuration of the `.conf` File

Create a `.conf` file in the main directory of the project with the following content:

```ini
[Credentials]
username = <The username for authentication>
password = <The password for authentication>

[Path]
app = <Path to the applcation to submit>
report = <Path where reports will be create>
```

Make sure to replace the empty fields with the appropriate values.  

## Setting the Path for Log and Report Folders

In the utils.py file, set the path of the folder where the log and HTML_reports folders will be created within the create_folders() method.

```python
def create_folders():
    import os
    
    directories = ["log","HTML_reports"]
    parent = "Your directory goes here"

    for dir in directories:
            
        path = os.path.join(parent, dir)
        if not os.path.isdir(path):
            
            os.makedirs(path)
            print(f"Folder Created {dir}")
        else:
            print("Exist folders!")
```

## Installation
Creating a Virtual Environment (venv)

It is recommended to create a virtual environment to manage the project's dependencies. Follow these steps:

<ul>
  <li>
    <p>Create a virtual environment:</p>
    
```sh
python -m venv venv
```
    
  </li>
  <li>
    <p>Activate the virtual environment:</p>  
    
```sh
On Windows ===> .\venv\Scripts\activate
On Linux   ===>  source venv/bin/activate
```
  </li>
  
  <li>
    <p>Install requirements</p>  
    
```sh
pip install -r requirements.txt
```
  </li>

  <li>
    <p>Run app.py</p>

```sh
python /src/app.py
```
  </li>
</ul>

## Additional Notes  

Ensure to keep the <b>.conf</b> file secure and do not commit it to a public repository.
Verify that all dependencies are listed in the requirements.txt file to ensure proper installation.

## Contact
For more information or assistance, contact Andrew Raieta at [andrewraieta@gmail.com].
