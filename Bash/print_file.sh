#!/bin/bash
#
# Name: dog-tor
# Prompt the employee for information and print the results.
#
# Prompt the user for the file name.
echo -e "Enter a file name with the pattern \"firstname_lastname.usr\""
read testDirFile

# Check to see if the file already exists before printing its contents.
if [ ! -e "test_users/$testDirFile" ];
then
	echo "file : <$testDirFile> does not exist."
else
	cat "test_users/$testDirFile"
fi
