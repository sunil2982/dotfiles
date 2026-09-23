#!/bin/bash

# Exit cleanly when the reader (e.g. waybar) closes the pipe
trap 'exit 0' SIGPIPE

SOUND_FILE_UPDATE="$HOME/.config/hypr/sounds/update.wav"
SOUND_FILE_ERROR="$HOME/.config/hypr/sounds/error.wav"
update_sign="$HOME/.config/hypr/icons/update.png"
done_sign="$HOME/.config/hypr/icons/done.png"
warning_sign="$HOME/.config/hypr/icons/warning.png"
error_sign="$HOME/.config/hypr/icons/error.png"
upd_script="$HOME/.config/hypr/scripts/pkgupdate.sh"

# Notification functions
update_notification() {
    notify-send -i "$1" "$2" "$3"
    [ -f "$SOUND_FILE_UPDATE" ] && paplay "$SOUND_FILE_UPDATE"
}

error_notification() {
    notify-send -i "$1" "$2" "$3"
    [ -f "$SOUND_FILE_ERROR" ] && paplay "$SOUND_FILE_ERROR"
}

# Function to check Arch updates safely
get_arch_updates() {
    local ofc=0 aur=0
    if command -v checkupdates &>/dev/null; then
        ofc=$(checkupdates | wc -l)
    fi
    
    local aurhlpr
    aurhlpr=$(command -v yay || command -v paru)
    if [ -n "$aurhlpr" ]; then
        aur=$($aurhlpr -Qua | wc -l)
    fi
    
    echo "$(( ofc + aur )) $ofc $aur"
}

check_update() {
    if [ -n "$(command -v pacman)" ]; then
        read -r upd ofc aur < <(get_arch_updates)

        if [ "$upd" -eq 0 ] ; then
            echo "{\"text\":\"$upd\", \"tooltip\":\"  Packages are up to date\"}"
        else
            echo "{\"text\":\"$upd\", \"tooltip\":\"󱓽 Official $ofc\n󱓾 AUR $aur\n\nPress click to update\"}"
        fi

    elif [ -n "$(command -v dnf)" ]; then
        upd=$(dnf check-update -q | grep -vE 'Last metadata expiration|^$' | wc -l)

        if [ "$upd" -eq 0 ] ; then
            echo "{\"text\":\"$upd\", \"tooltip\":\"  Packages are up to date\"}"
        else
            echo "{\"text\":\"$upd\", \"tooltip\":\"󱓽 Updates Available: $upd\n\nPress click to update\"}"
        fi

    elif [ -n "$(command -v zypper)" ]; then
        upd=$(zypper lu --best-effort | grep -c 'v  |')

        if [ "$upd" -eq 0 ] ; then
            echo "{\"text\":\"$upd\", \"tooltip\":\"  Packages are up to date\"}"
        else
            echo "{\"text\":\"$upd\", \"tooltip\":\"󱓽 Updates Available: $upd\n\nPress click to update\"}"
        fi
    fi
}

package_update() {
    if [ -n "$(command -v pacman)" ]; then
        kitty --title update sh -c "${upd_script}"
        read -r upd _ _ < <(get_arch_updates)

        sleep 1

        if [ "$upd" -eq 0 ]; then
            update_notification "$done_sign" "Done" "Packages have been updated"
        elif [ "$upd" -gt 0 ]; then
            error_notification "$warning_sign" "Warning!" "Some packages may have been skipped"
        else
            error_notification "$error_sign" "Error!" "Sorry, could not update packages"
        fi

    elif [ -n "$(command -v dnf)" ]; then
        kitty --title update sh -c "${upd_script}"
        upd=$(dnf check-update -q | grep -vE 'Last metadata expiration|^$' | wc -l)

        sleep 1

        if [ "$upd" -eq 0 ]; then
            update_notification "$done_sign" "Done" "Packages have been updated"
        elif [ "$upd" -gt 0 ]; then
            error_notification "$warning_sign" "Warning!" "Some packages may have been skipped"
        else
            error_notification "$error_sign" "Error!" "Sorry, could not update packages"
        fi

    elif [ -n "$(command -v zypper)" ]; then
        kitty --title update sh -c "${upd_script}"
        upd=$(zypper lu --best-effort | grep -c 'v  |')

        sleep 1

        if [ "$upd" -eq 0 ]; then
            update_notification "$done_sign" "Done" "Packages have been updated"
        elif [ "$upd" -gt 0 ]; then
            error_notification "$warning_sign" "Warning!" "Some packages may have been skipped"
        else
            error_notification "$error_sign" "Error!" "Sorry, could not update packages"
        fi
    fi

    # Trigger Waybar signal update instead of full reload if supported
    pkill -RTMIN+8 waybar || "$HOME/.config/hypr/scripts/waybar-reload.sh" --reload
}

# Default to --check if no argument is provided
case "${1:---check}" in
    --check)
        check_update
        ;;
    --update)
        package_update
        ;;
    *)
        check_update
        ;;
esac