#!/bin/bash

echo "Downloafind required packages..."
apt-get install -y python3-pip > /dev/null
# user=$(grep kEye /etc/passwd)
# if [[ ${#user} -lt 10 ]]
# then
#     useradd kEye > /dev/null
#     echo "kEye ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/kEye
# fi
echo "Validating config files...";
python3 app/validator.py
if [ $? -ne 0 ]
then
    exit 1
fi
echo "Creating virtual environment..."
pip -q install virtualenv
# delete the current virtual environment if exists
currenv=$(ls | grep kEvenv)
if [[ ${#currenv} -ge 6 ]]
then
    rm -rf kEvenv > /dev/null
fi
virtualenv kEvenv > /dev/null
source ./kEvenv/bin/activate
pip -q install -r requirements.txt
cp -r app  conf libexec  kEvenv/ 
cp server.py kEvenv/
cd kEvenv
echo "Running the server..."
gunicorn --bind 127.0.0.1:21393 server:app --daemon




