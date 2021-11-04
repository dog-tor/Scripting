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
echo "" # Print an empty line
echo -e "User's Full Name   :" $userFullName
echo -e "User's ID\t   :" $userID
echo -e "User's Job Location:" $userJobLocation
echo -e "User's Manager Code:" $userManagerCode
