#!/bin/bash

# Fallback styles in case they aren't defined elsewhere
pos=""
r_override=""
fnt_override=""

case $1 in
    c)
        selected=$(cliphist list | rofi -dmenu -config ~/.config/rofi/rofi-clipboard.rasi)
        if [ -n "$selected" ]; then
            echo "$selected" | cliphist decode | wl-copy
        fi
        ;;
    w)  
        # Clear clipboard history with a confirmation prompt
        if [ "$(echo -e "Yes\nNo" | rofi -dmenu -config ~/.config/rofi/rofi-clipboard.rasi \
            -theme-str "entry { placeholder: \"Clear Clipboard History?\";} ${pos} ${r_override}" \
            -theme-str "${fnt_override}" \
            -config ~/.config/rofi/rofi-clipboard.rasi)" == "Yes" ] ; then
            cliphist wipe
        fi
        ;;
    l)  
        # Show number of items
        cliphist list | wc -l
        ;;
    *)  
        echo -e "cliphist.sh [action]"
        echo "c :  cliphist list and copy selected"
        echo "w :  cliphist wipe database"
        echo "l :  show the number of items in the clipboard"
        exit 1
        ;;
esac