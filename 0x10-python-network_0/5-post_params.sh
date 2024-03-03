#!/bin/bash
#send email and subject

curl -sd "subject=I will always be here for PLD" -d "body=Email body" "test@gmail.com"
