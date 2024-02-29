#!/bin/bash
# Check if URL argument is provided
curl -s "$1" | wc -c