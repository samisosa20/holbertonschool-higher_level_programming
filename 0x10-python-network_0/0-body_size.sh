#!/bin/bash
# return the body size of url
curl -w '%{size_download}\n' -so /dev/null $1
