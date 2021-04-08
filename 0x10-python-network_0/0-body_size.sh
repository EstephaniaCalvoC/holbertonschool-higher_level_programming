#!/bin/bash
# Displays the size of the body content of indicated URL.
curl -sI "$1" | grep Content-Length | cut -d" " -f2 
