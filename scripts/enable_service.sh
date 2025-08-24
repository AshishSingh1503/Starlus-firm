#!/usr/bin/env bash
set -euo pipefail
sudo cp systemd/pen.service /etc/systemd/system/pen.service
sudo cp systemd/pen-ota.service /etc/systemd/system/pen-ota.service
sudo cp systemd/pen-ota.timer /etc/systemd/system/pen-ota.timer
sudo systemctl daemon-reload
sudo systemctl enable pen.service
sudo systemctl enable pen-ota.timer
sudo systemctl start pen.service
sudo systemctl start pen-ota.timer