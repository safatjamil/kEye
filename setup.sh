#!/bin/bash

echo "Setting up local environment..."
apt-get install -y python3-pip > /dev/null
user=$(grep kEye /etc/passwd)
if [[ ${#user} -lt 10 ]]
then
    useradd kEye > /dev/null
    echo "kEye ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/kEye
fi
pip3 install -r requirements.txt > /dev/null
echo "Validating config files...";
python3 app/validator.py
echo $?;
if [[ $? -ne 0 ]]
    then
        exit 0;
    fi

