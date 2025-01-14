#!/bin/bash
xinput set-prop "ELAN06FA:00 04F3:32B9 Touchpad" "libinput Tapping Enabled" 1
picom --daemon &
nitrogen --restore &
