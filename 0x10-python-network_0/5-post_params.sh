#!/bin/bash
#send email and subject

curl -sd "email=test@gmail.com" -d "subject=I will always be here for PLD" $@
