#!/bin/bash

# Fallback styles in case they aren't defined elsewhere
pos=""
r_override=""
fnt_override=""

case $1 in
    c)
        # Added -location 3 directly to force top-right positioning in dmenu mode
        selected=$(cliphist list | awk -F'\t' '{print $2}' | rofi -dmenu -config ~/.config/rofi/rofi-clipboard.rasi -location 3)
        if [ -n "$selected" ]; then
            cliphist list | grep --fixed-strings "$selected" | head -n 1 | cliphist decode | wl-copy
        fi
        ;;
    w)  
        # Clear clipboard history with a confirmation prompt (also added -location 3)
        if [ "$(echo -e "Yes\nNo" | rofi -dmenu -config ~/.config/rofi/rofi-clipboard.rasi -location 3 \
            -theme-str "entry { placeholder: \"Clear Clipboard History?\";} ${pos} ${r_override}" \
            -theme-str "${fnt_override}" )" == "Yes" ] ; then
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