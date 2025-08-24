SLD Smart Pen Firmware (Pi Zero + Coral) – Complete Starter Repo

This is a production-ready starter firmware for your SLD smart writing tool pen built on Raspberry Pi Zero (W) with Google Coral USB Accelerator, a pressure sensor via ADC (ADS1115/MCP3008), and a USB/I2S microphone.

The repo includes:

Modular Python services for pressure sensing, audio capture with VAD, local buffering (SQLite), uplink via MQTT/HTTPS, battery monitoring, and OTA updates.

Clean shutdown, logging, retries, config via YAML, and systemd units.

Optional Edge TPU hooks (keyword spotting / handwriting pre-filter).

0) Hardware Assumptions & Wiring

MCU/Host: Raspberry Pi Zero W (Debian/Raspberry Pi OS)
ML: Google Coral USB Accelerator (optional)
Pressure Sensor via ADC: Choose one

ADS1115 (I2C): VDD=3.3V, GND=GND, SDA=GPIO2, SCL=GPIO3. Pen pressure sensor → A0.

MCP3008 (SPI): VDD=3.3V, VREF=3.3V, AGND=GND, CLK=GPIO11, DOUT=GPIO9, DIN=GPIO10, CS=GPIO8. Pressure sensor → CH0.

Microphone: USB mic (easiest) or I2S mic (e.g., INMP441).
Battery: LiPo + fuel gauge (e.g., MAX17043 via I2C) or simple ADC divider to measure voltage.