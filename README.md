# Edit services.toml
Enter your services you want to monitor. Please check the existing services.toml file.

# Api
You can restrain anyone from accessing this server. You can set the api users who can access this.

# Web
Web interface is not available right now.

# Custom check
There are 3 checks configured now. You can write your own custom check. However make sure it triggers the correct output and exit code. 
Exit code 0 will return a response code 200. Anything other than that will return 503.

# Port
It runs on a lightweight flask server on port 21393. You can change this port in setup.sh

# Running this as a service
It will be better if you run this under systemd
