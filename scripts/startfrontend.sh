#!/bin/bash
IP=$(ip -4 addr show wlan0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
cd ../room-beer-vue/
VUE_APP_IP=$IP npm run serve