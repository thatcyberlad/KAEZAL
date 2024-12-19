#!/bin/bash

# Define the banners
figlet_banner=$(cat << 'EOF'
_  _ ____ _        _  _ ____ ____ _  _ 
|  | |__/ |        |\/| |__| [__  |_/  
|__| |  \ |___ ___ |  | |  | ___] | \_ 
                                       
EOF
)

banner=$(cat << 'EOF'
   Created by Team KAEZAL
EOF
)

# Print banners
print_banners() {
    echo "$figlet_banner"
    echo "$banner"
    printf ""
}

# Validate the URL format
validate_web_url() {
    local url="$1"
    if [[ ! "$url" =~ ^https?://([a-zA-Z0-9-]+\.)+([a-zA-Z]{2,})(:[0-9]{1,5})?(/.*)?$ ]]; then
        echo "Invalid URL format. Please provide a valid web URL." >&2
        return 1
    fi
    return 0
}

# Validate the custom domain
validate_custom_domain() {
    local domain="$1"
    if [[ ! "$domain" =~ ^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
        echo "Invalid custom domain. Please provide a valid domain name." >&2
        return 1
    fi
    return 0
}

# Validate phishing keywords
format_phish_keywords() {
    local keywords="$1"
    local max_length=15

    if [[ "$keywords" =~ \  ]]; then
        echo "Phishing keywords should not contain spaces. Use '-' to separate them." >&2
        return 1
    fi

    if [[ "${#keywords}" -gt $max_length ]]; then
        echo "Input string exceeds the maximum allowed length." >&2
        return 1
    fi

    echo "$keywords" | sed 's/ /-/g'
    return 0
}

# Mask URL with custom domain and phishing keywords
mask_url() {
    local domain="$1"
    local keyword="$2"
    local url="$3"
    local scheme
    local netloc
    local path

    scheme=$(echo "$url" | awk -F '://' '{print $1}')
    netloc=$(echo "$url" | awk -F '://' '{print $2}' | awk -F '/' '{print $1}')
    path=$(echo "$url" | awk -F "$netloc" '{print $2}')

    echo "$scheme://$domain-$keyword@$netloc$path"
}

# Main script logic
print_banners

while true; do
    # Get URL input
    while true; do
        read -rp "Enter the original link (ex: https://www.ngrok.com) or type 'exit' to quit: " web_url
        if [[ "$web_url" == "exit" ]]; then
            echo "Goodbye!"
            exit 0
        fi
        validate_web_url "$web_url" && break
    done

    # Get custom domain
    while true; do
        read -rp "Enter your custom domain (ex: gmail.com) or type 'exit' to quit: " custom_domain
        if [[ "$custom_domain" == "exit" ]]; then
            echo "Goodbye!"
            exit 0
        fi
        validate_custom_domain "$custom_domain" && break
    done

    # Get phishing keywords
    while true; do
        read -rp "Enter phishing keywords (ex: free-stuff, login) or type 'exit' to quit: " phish
        if [[ "$phish" == "exit" ]]; then
            echo "Goodbye!"
            exit 0
        fi
        formatted_phish=$(format_phish_keywords "$phish")
        [[ $? -eq 0 ]] && break
    done

    # URL shortener services (mocked for demonstration)
    shorteners=("tinyurl" "dagd" "clckru" "osdb")

    # Simulate URL shortening and print results immediately
    echo -e "\nOriginal URL: $web_url\n"
    echo "[~] Masked URLs:"
    for shortener in "${shorteners[@]}"; do
        shortened_url="$web_url/$shortener"
        masked_url=$(mask_url "$custom_domain" "$formatted_phish" "$shortened_url")
        echo "╰➤ $masked_url"
        printf ""
    done

    # Option to continue or exit
    read -rp "Do you want to mask another URL? (yes/no): " choice
    if [[ "$choice" != "yes" ]]; then
        echo "Goodbye!"
        break
    fi
done
