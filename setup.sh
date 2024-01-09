#!/bin/bash
echo "Setting up virtual environment"
apt-get install -y python-pip > /dev//nul
pip install virtualenv
rm -r kEye
virtualenv kEye

echo "Validating config files";
python3 app/validator.py
echo $?;
if [[ $? -ne 0 ]]
    then
        exit 0;
    fi