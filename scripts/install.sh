#!/bin/bash
cp roombeer-stream.service /etc/systemd/system/
cp roombeer-frontend.service /etc/systemd/system/
cp roombeer-backend.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable roombeer-stream.service
systemctl start roombeer-stream.service
systemctl enable roombeer-frontend.service
systemctl start roombeer-frontend.service
systemctl enable roombeer-backend.service
systemctl start roombeer-backend.service
