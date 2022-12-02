# Perspective-Configuration-Tool
Application used to create perspectives based on configuration files. These perspectives can be used within the CM-API to create new communities and analyze them within the VISOR application.  

# Usage
Requirements: 
- Config-Tool (https://github.com/angelsanmar/Perspective-Configuration-Tool)
- Latest version of Python (https://www.python.org/downloads/)

Execution:  
- Open CMD inside /configuration-tool/configuration-tool/ folder and enter the following to run python server:
``` 
python -m http.server
```
- The app will be avalible at ```http://localhost:8000```

# Tool Configuration:
The user can define the use of the local or remote seed file from the CM-API, and also define the host address of the CM-API.  
To do so, you need to edit the ```configToolSetup.json``` file as desired. 
