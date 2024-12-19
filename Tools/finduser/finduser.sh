#!/bin/sh

# Color codes
RED='\033[1;91m'
GREEN='\033[1;92m'
YELLOW='\033[1;93m'
BLUE='\033[1;94m'
CYAN='\033[1;96m'
WHITE='\033[1;97m'
RESET='\033[0m'

# Banner
printf "${CYAN}
 _______ _____ __   _ ______  _     _ _______ _______  ______
 |______   |   | \  | |     \ |     | |______ |______ |_____/
 |       __|__ |  \_| |_____/ |_____| ______| |______ |    \_
${RESET}

${YELLOW}Created by Team KAEZAL${RESET}\n\n"

# Input IP address
printf "${WHITE}Enter User's IP Address: ${RESET}"
read ip_address

# Validate IP address input
if [ -z "$ip_address" ]; then
  printf "\n${RED}Error:${RESET} No IP address entered. Exiting.\n"
  exit 1
fi

# Fetch IP details
printf "\n${BLUE}Fetching details for IP: ${WHITE}$ip_address${RESET}...\n\n"
response=$(curl -s -w "%{http_code}" -o /tmp/ipinfo.json "https://ipinfo.io/$ip_address")

# Check HTTP status code
http_status=$(tail -c 3 /tmp/ipinfo.json)
if [ "$http_status" -ne 200 ]; then
  printf "${RED}Error:${RESET} Failed to fetch details. HTTP Status: $http_status\n"
  printf "${RED}Suggestion:${RESET} Check the IP address or your internet connection.\n"
  exit 1
fi

# Parse and display details
details=$(cat /tmp/ipinfo.json | head -n -1)
if [ -z "$details" ]; then
  printf "${RED}Error:${RESET} No data found for the provided IP address.\n"
  exit 1
fi

# Display details
printf "${GREEN}IP Details:${RESET}\n"
printf "${CYAN}%s${RESET}\n" "$details"

# End message
printf "\n${GREEN}Task completed successfully.${RESET}\n"

# Clean up temporary file
rm -f /tmp/ipinfo.json
