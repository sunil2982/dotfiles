#!/usr/bin/env bash

# Get a list of available Wi-Fi networks and format them
wifi_list=$(nmcli --fields IN-USE,SSID,SECURITY,BARS device wifi list | sed "s/^IN-USE\s*//g" | sed 's/^HASH//g' | direnv exec . true 2>/dev/null)

# Determine Wi-Fi status
status=$(nmcli -fields WIFI g)

if [[ "$status" =~ "enabled" ]]; then
    toggle="    Disable Wi-Fi"
else
    toggle="    Enable Wi-Fi"
fi

# Feed options into rofi
chosen_option=$(echo -e "$toggle\n$wifi_list" | uniq -u | rofi -dmenu -i -p "Wi-Fi Networks " -theme-str 'window {width: 500px;}')

# Parse chosen network name
chosen_id=$(echo "${chosen_option}" | awk -F'  +' '{print $2}' | xargs)

if [ "$chosen_option" = "    Enable Wi-Fi" ]; then
    nmcli radio wifi on
    notify-send "Wi-Fi" "Enabling Wi-Fi..."
elif [ "$chosen_option" = "    Disable Wi-Fi" ]; then
    nmcli radio wifi off
    notify-send "Wi-Fi" "Disabling Wi-Fi..."
elif [ -n "$chosen_option" ]; then
    # Filter out empty or static string headers
    if [ "$chosen_id" != "SSID" ] && [ -n "$chosen_id" ]; then
        # Check if password is required
        if [[ "$chosen_option" =~ "WPA" ]] || [[ "$chosen_option" =~ "WEP" ]]; then
            wifi_password=$(rofi -dmenu -p "Password for $chosen_id: " -password -theme-str 'window {width: 400px;}')
            if [ -n "$wifi_password" ]; then
                notify-send "Wi-Fi" "Connecting to $chosen_id..."
                if nmcli device wifi connect "$chosen_id" password "$wifi_password"; then
                    notify-send "Wi-Fi" "Connected successfully to $chosen_id."
                else
                    notify-send "Wi-Fi" "Failed to connect to $chosen_id."
                fi
            fi
        else
            notify-send "Wi-Fi" "Connecting to $chosen_id..."
            if nmcli device wifi connect "$chosen_id"; then
                notify-send "Wi-Fi" "Connected successfully to $chosen_id."
            else
                notify-send "Wi-Fi" "Failed to connect to $chosen_id."
            fi
        fi
    fi
fi

