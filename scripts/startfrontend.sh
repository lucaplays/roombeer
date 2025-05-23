#!/bin/bash

IP=""
while [ -z $IP ]; do
    IP=$(ip -4 addr show wlan0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
    sleep 1
done

cd ../room-beer-vue/
npm install
echo "Running on $IP"
VUE_APP_IP=$IP npm run serve