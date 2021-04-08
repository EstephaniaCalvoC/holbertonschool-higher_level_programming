#!/bin/bash
# Display the body of the response sending 2 variables with a POST request.
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST "$1"
