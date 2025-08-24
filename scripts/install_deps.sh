#!/usr/bin/env bash
set -euo pipefail
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv python3-dev \
portaudio19-dev alsa-utils git libatlas-base-dev \
libffi-dev libssl-dev


python3 -m venv /opt/pen-venv
source /opt/pen-venv/bin/activate
pip install --upgrade pip wheel
pip install -r requirements.txt


sudo mkdir -p /var/lib/pen/audio /var/lib/pen
sudo chown -R $(whoami):$(whoami) /var/lib/pen


echo "Done."