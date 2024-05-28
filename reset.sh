#!/bin/bash

# Color definitions
GREEN="\e[32m"
IGREEN="\e[92m"
IYELLOW="\e[93m"
CLEAR="\e[0m"

CONFIG_FILE="$HOME/.sharepyfx/sharepyfx.py"

# Function to update the configuration
update_config() {
    local token="$1"
    local id="$2"
    
    # Use sed to update the configuration file
    sed -i "s/^BOT_TOKEN = .*/BOT_TOKEN = '$token'/g" "$CONFIG_FILE"
    sed -i "s/^ATTACKER_ID = .*/ATTACKER_ID = '$id'/g" "$CONFIG_FILE"

    echo -e "${GREEN}[${IGREEN}✔${CLEAR}${GREEN}] ${IYELLOW}Configuration updated successfully.${CLEAR}"
}

# Check if the configuration file exists
if [[ ! -f "$CONFIG_FILE" ]]; then
    echo -e "${GREEN}[${IGREEN}✘${CLEAR}${GREEN}] ${IYELLOW}Configuration file not found: $CONFIG_FILE${CLEAR}"
    exit 1
fi

# Prompt the user for the new BOT_TOKEN
echo -e -n "${GREEN}[${IGREEN}➜${CLEAR}${GREEN}] ${IYELLOW}Enter new BOT_TOKEN: ${CLEAR}"
read -r new_token

# Prompt the user for the new ATTACKER_ID
echo -e -n "${GREEN}[${IGREEN}➜${CLEAR}${GREEN}] ${IYELLOW}Enter new ATTACKER_ID: ${CLEAR}"
read -r new_id

# Update the configuration
update_config "$new_token" "$new_id"
