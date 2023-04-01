#!/bin/bash
# Script that sent a get request to URS and display the body
curl sI "$1" | grep "Content-Length:" | cut -d " " -f 2
