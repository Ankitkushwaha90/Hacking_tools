#!/bin/bash

macchanger -l > vendormac.txt
ouimac=$(shuf -n 1 vendormac.txt | awk '{print$3}')
uaamac=$(printf '%02x:%02x:%02x' $[RANDOM%256] $[RANDOM%256] $[RANDOM%256])
macchanger -m  "$ouimac:$uaamac" eth0

