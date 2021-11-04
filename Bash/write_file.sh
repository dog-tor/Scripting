#!/bin/bash
#
# Name: dog-tor
# Prompt the employee for information and print the results.
#
echo -e "Enter User's Full Name \t  : <Enter a first name B last name; alpha and space only>" 
read userFullName
echo -e "Enter User's ID\t\t  : <Enter a 6 digit number; digits only>" 
read userID
echo -e "Enter User's Job Location : <Enter 4 characters>  [Make sure to enter AA99 pattern job location, eg: BX56, CR91]" 
read userJobLocation
echo -e "Enter User's Manager Code : <Enter a 6 digit number; digits only>" 
read userManagerCode
echo "" # Print a new line.

file="$(echo $userFullName | sed 's/ /_/g').usr" # Create a new variable for the file name.

if [ ! -d "test_users" ]; # Check to see if the directory exists.
then
	mkdir test_users
fi

# Print the user's information to the screen and use tee to add the data to the file as well.
echo -e "User's Full Name   :" $userFullName | tee test_users/"$file"
echo -e "User's ID\t   :" $userID | tee -a test_users/"$file"
echo -e "User's Job Location:" $userJobLocation | tee -a test_users/"$file"
echo -e "User's Manager Code:" $userManagerCode | tee -a test_users/"$file"

# Inform the user of where their new file is saved.
echo "$file file has been created at test_users/$file"

