#!/bin/bash
picom --daemon &
nitrogen --restore &
dunst & 
bash ~/scripts/battery_warning.sh & 
notify-send -u critical "upload the configs, update the package names, and be aware what you become"
notify-send "You can not touch that with the words"
sudo ip link set wlan0 down
sudo iw dev wlan1 set power_save off
