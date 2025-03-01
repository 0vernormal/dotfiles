#!/bin/bash

NOTIFY_CMD="notify-send -u critical 'BATTERY WARNING!'"
THRESHOLDS=(40 30 20 10 5 1)
PREVIOUS_LEVEL=100

while true; do
    BATTERY_INFO=$(acpi -b)
    BATTERY_STATUS=$(echo "$BATTERY_INFO" | awk '{print $3}' | tr -d ',')
    BATTERY_LEVEL=$(echo "$BATTERY_INFO" | awk '{print $4}' | tr -d '%,')
    REMAINING_TIME=$(echo "$BATTERY_INFO" | awk -F', ' '{print $3}')

    for THRESHOLD in "${THRESHOLDS[@]}"; do
        if [[ "$BATTERY_LEVEL" -le "$THRESHOLD" && "$PREVIOUS_LEVEL" -gt "$THRESHOLD" ]]; then
            eval "$NOTIFY_CMD 'Battery level is $BATTERY_LEVEL%! $REMAINING_TIME'"
            PREVIOUS_LEVEL=$BATTERY_LEVEL
        fi
    done

    sleep 60
done
