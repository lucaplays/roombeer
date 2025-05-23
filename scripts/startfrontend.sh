#!/bin/bash

IP=""
while [ -z $IP ]; do
    IP=$(ip -4 addr show wlan0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
    sleep 1
done

cd ../room-beer-vue/
npm install
VUE_APP_IP=$IP npm run build
npx http-serve dist/ -p 8080