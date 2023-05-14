#!/bin/bash
# Script that sends a POST request and displays the body response
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
