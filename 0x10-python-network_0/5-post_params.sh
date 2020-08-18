#!/bin/bash
# Sends a POST request to the URL with certain variables
curl $1 -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
