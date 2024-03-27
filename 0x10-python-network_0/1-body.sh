#!/bin/bash

# Function to send GET request to the provided URL and display body
get_url_body() {
    # Send GET request using curl and store response headers and body in separate files
    curl -sS -D headers.txt -o body.txt "$1"

    # Extract status code from response headers
    status_code=$(grep "HTTP/" headers.txt | awk '{print $2}')

    # Check if status code is 200
    if [[ "$status_code" == "200" ]]; then
        # Display body of the response
        cat body.txt
    else
        echo "Error: Status code $status_code"
    fi

    # Clean up temporary files
    rm headers.txt body.txt
}

# Check if a URL is provided as an argument
if [[ $# -eq 0 ]]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Call function to get URL body
get_url_body "$1"
