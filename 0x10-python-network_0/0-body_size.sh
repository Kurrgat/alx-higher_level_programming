#!/bin/bash

# Check if the user provided a URL
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
URL=$1

# Send a request to the URL using curl and get the size of the body of the response
response=$(curl -s -o /dev/null -w "%{size_download}" "$URL")

# Display the size of the body of the response in bytes
echo "Size of the response body: $response bytes"
