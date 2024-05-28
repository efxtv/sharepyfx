#!/bin/bash

chmod +x ~/.sharepyfx/bin/sharepyfx
chmod +x ~/.sharepyfx/*

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Detect the operating system
if command_exists termux-info; then
    OS="Termux"
elif command_exists lsb_release; then
    OS=$(lsb_release -si)
else
    OS=$(uname -s)
fi

# Make scripts executable
chmod +x sharepyfx.py
chmod +x bin/sharepyfx

# Create symbolic link based on the operating system
case "$OS" in
    "Termux")
        ln -s $PWD/bin/sharepyfx $PREFIX/bin/
        ;;
    "Ubuntu" | "Debian" | "Kali" | "Arch" | "Manjaro" | "Fedora")
        sudo ln -s $PWD/bin/sharepyfx /usr/local/bin/
        ;;
    *)
        echo "Unsupported OS: $OS"
        exit 1
        ;;
esac

echo "Installation complete."
