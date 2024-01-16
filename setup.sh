#!/bin/bash
echo "Checking required packages..."
sudo apt-get install -y python3-pip > /dev/null
echo "Validating config files...";
python3 main/validator.py
if [ $? -ne 0 ]
then
    exit 1
fi
echo "Creating virtual environment..."
pip -q --disable-pip-version-check install virtualenv
# delete the current virtual environment if exists
currenv=$(ls | grep kEvenv)
if [[ ${#currenv} -ge 6 ]]
then
    rm -rf kEvenv > /dev/null
fi
virtualenv kEvenv > /dev/null
source ./kEvenv/bin/activate
pip -q --disable-pip-version-check install -r requirements.txt
cp -r conf main libexec kEvenv/ 
chmod +r kEvenv/conf/*
chmod +r kEvenv/main/*
chmod +x kEvenv/main/*
chmod +r kEvenv/libexec/*
chmod +x kEvenv/libexec/*
cp server.py kEvenv/
chmod +x kEvenv/server.py
cd kEvenv
echo "Running the server..."
gunicorn --bind 127.0.0.1:21393 server:app --daemon




