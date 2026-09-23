How to use it when you reinstall Arch Linux:

Once you wipe and reinstall Arch Linux, restoring your setup will only take a couple of commands:

    Install git on your fresh Arch install:
    Bash

    sudo pacman -S git

    Clone your repository anywhere on your system (e.g., your home directory):
    Bash

    git clone https://github.com/USERNAME/repository-name.git ~/dotfiles

    Navigate into the cloned folder and run your installation script:
    Bash

    cd ~/dotfiles
    chmod +x install.sh
    ./install.sh

(Note: Ensure your install.sh script is programmed to automatically copy or symlink your configuration files from the repo folder into your system's proper paths, like ~/.config/hypr/).
