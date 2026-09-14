#!/bin/bash

# Colors for terminal styling
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
CYAN='\033[1;36m'
NC='\033[0m' # No Color

clear
echo -e "${CYAN}======================================================${NC}"
echo -e "${GREEN}       HERO.PY - SETUP & INSTALLATION WIZARD          ${NC}"
echo -e "${CYAN}======================================================${NC}"

# Step 1: Update and Upgrade packages
echo -e "\n${YELLOW}[*] Updating Termux packages...${NC}"
pkg update -y && pkg upgrade -y

# Step 2: Install Python and Git if not available
echo -e "\n${YELLOW}[*] Installing Python and required dependencies...${NC}"
pkg install python git -y

# Step 3: Install required Python modules
echo -e "\n${YELLOW}[*] Installing Python modules (json, os, etc.)...${NC}"
pip install --upgrade pip

# Step 4: Setting up execution permission for hero.py
if [ -f "hero.py" ]; then
    chmod +x hero.py
    echo -e "\n${GREEN}[+] Permission granted successfully for hero.py!${NC}"
else
    echo -e "\n${RED}[!] Warning: hero.py not found in the current directory.${NC}"
fi

echo -e "\n${CYAN}======================================================${NC}"
echo -e "${GREEN}[+] Installation Completed Successfully (v1.2 Beta)!${NC}"
echo -e "${YELLOW}[*] To run your tool, type: python hero.py${NC}"
echo -e "${CYAN}======================================================${NC}"
