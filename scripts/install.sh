#!/bin/bash
cp roombeer-stream.service /etc/systemd/system/roombeer-stream.service
sudo systemctl daemon-reload
sudo systemctl enable roombeer-stream.service
sudo systemctl start roombeer-stream.service
