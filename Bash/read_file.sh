#!/bin/bash
#
# Name: dog-tor
# Prompt the employee for information and print the results.
#
echo -e "Enter a file name with the pattern \"firstname_lastname.usr\"" # Prompt the user for the file name.
read testDirFile

cat "test_users/$testDirFile" # display the contents of the entered file.
