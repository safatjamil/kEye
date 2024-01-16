#!/bin/bash
service=$1
status=$(systemctl show -p SubState --value $service)
if [[ $status = *'running'* ]]
then
    echo "$service is running"
    exit 0
else
    echo "$service is not running"
    exit 1
fi
