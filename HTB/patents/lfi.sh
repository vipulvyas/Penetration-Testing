#!/bin/bash

HOST=10.10.10.173
FILE=$1
URL="http://$HOST/getPatent_alphav1.0.php?id=....//....//....//....//....//$FILE"

curl -s \
     $URL \
| sed '/<pre>/,/<\/pre>/!d' \
| sed 1,4d \
| xmllint --recover --xpath "//pre" - 2>/dev/null \
| sed -r 's/<\/?pre\/?>//g'

