# Edit services.toml
Enter your services you want to monitor. Please check the existing conf/services.toml file.

# Api Users
You can restrain anyone from accessing this server. You can set the api users who can access this. Edit conf/api.yml file.

# Web Users
Web interface is not available right now.

# Custom check
There are 3 checks configured now. You can write your own custom check. However make sure it triggers the correct output and exit code. 
Exit code 0 will return a response code 200. Anything other than that will return 503. Put your custom scripts in the libexec directory.

# Port
It runs on a lightweight flask server on port 21393. You can change this port in setup.sh file.

# Running this as a service
It will be better if you run this under systemd.

# Api Reference
$(host ip or domain)/api/$(service name)/status/ ; Only GET method is allowed.
