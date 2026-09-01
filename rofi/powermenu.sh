#!/usr/bin/env bash

# Current Theme
dir="$HOME/.config/rofi"
theme='powermenu'

# Options
shutdown='󰐥'
reboot='󰜉'
lock='󰌾'
suspend='󰤄'
logout='󰍃'

# Rofi CMD
rofi_cmd() {
	rofi -dmenu \
		-p "Goodbye $USER" \
		-mesg "Uptime: $(uptime -p | sed -e 's/up //')" \
		-theme "${dir}/${theme}.rasi"
}

# Pass variables to rofi dmenu
run_rofi() {
	echo -e "$lock\n$suspend\n$logout\n$reboot\n$shutdown" | rofi_cmd
}

# Actions
run_cmd() {
	if [[ "$1" == '--shutdown' ]]; then
		systemctl poweroff
	elif [[ "$1" == '--reboot' ]]; then
		systemctl reboot
	elif [[ "$1" == '--suspend' ]]; then
		systemctl suspend
	elif [[ "$1" == '--logout' ]]; then
		hyprctl dispatch exit
	elif [[ "$1" == '--lock' ]]; then
		hyprlock
	fi
}

# Actions
chosen="$(run_rofi)"
case ${chosen} in
    $shutdown)
		run_cmd --shutdown
        ;;
    $reboot)
		run_cmd --reboot
        ;;
    $lock)
		run_cmd --lock
        ;;
    $suspend)
		run_cmd --suspend
        ;;
    $logout)
		run_cmd --logout
        ;;
esac
