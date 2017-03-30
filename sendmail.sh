#!/bin/bash
# script to send simple email 
SUBJECT="Good Morning!"
EMAIL="klauke9@gmail.com"
EMAILMESSAGE="digest.txt"
# send an email using /bin/mail
mail -s "$SUBJECT" "$EMAIL" < $EMAILMESSAGE
