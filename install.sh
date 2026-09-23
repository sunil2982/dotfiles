#!/bin/bash
set -e

echo "Installing official packages via pacman..."
sudo pacman -S --needed hyprland waybar kitty rofi-wayland waypaper swaync starship git

echo "Installing AUR packages via yay..."
yay -S --needed matugen awww-git

echo "Creating configuration directory..."
mkdir -p ~/.config

echo "Linking configuration folders..."
ln -sfn ~/dotfiles/hypr ~/.config/hypr
ln -sfn ~/dotfiles/waybar ~/.config/waybar
ln -sfn ~/dotfiles/kitty ~/.config/kitty
ln -sfn ~/dotfiles/rofi ~/.config/rofi
ln -sfn ~/dotfiles/matugen ~/.config/matugen
ln -sfn ~/dotfiles/waypaper ~/.config/waypaper

echo "Restoring wallpaper and applying themes..."
waypaper --restore

echo "Arch Linux Hyprland setup complete!"
