#!/bin/bash
# script to send simple email 
SUBJECT="Good Morning!"
EMAIL="klauke9@gmail.com"
EMAILMESSAGE="digest.txt"
echo "This is an email message test"> $EMAILMESSAGE
# send an email using /bin/mail
/bin/mail -s "$SUBJECT" "$EMAIL" < $EMAILMESSAGE
