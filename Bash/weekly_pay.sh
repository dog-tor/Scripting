#!/bin/bash
#
# Name: dog-tor
# This program will prompt the user for their role and determine their weekly pay.

# Create the Variables
userInput=
CASUAL_RATE=8.25
PERM_RATE=12.50
STAFF_RATE=20

# Prompt the user for the information
echo "ABC Enterprises - Weekly Pay Calculation Process"
read -p "Enter Employee Category (C, P or S. 0 to quit): " userInput
    
while [ "$userInput" != "0" ] # Run the loop if the user does not enter a 0
do
    if [ $userInput == "C" ]
    then
        read -p "Enter hours worked: " hoursWorked
	weeklyPay=$(echo "$hoursWorked*$CASUAL_RATE" | bc -l)
        echo "Calculated Weekly Pay @8.25/hr = $ $weeklyPay"
	echo ""
        echo "ABC Enterprises - Weekly Pay Calculation Process"
        read -p "Enter Employee Category (C, P or S. 0 to quit): " userInput
    elif [ $userInput == "P" ]
    then
        read -p "Enter hours worked: " hoursWorked
	weeklyPay=$(echo "$hoursWorked*$PERM_RATE" | bc -l)
    	echo "Calculated Weekly Pay @12.5/hr = $ $weeklyPay"
	echo ""
        echo "ABC Enterprises - Weekly Pay Calculation Process"
        read -p "Enter Employee Category (C, P or S. 0 to quit): " userInput
    elif [ $userInput == "S" ]
    then	
        read -p "Enter hours worked: " hoursWorked
	weeklyPay=$(echo "$hoursWorked*$STAFF_RATE" | bc -l)
    	echo "Calculated Weekly Pay @20.0/hr = $ $weeklyPay"
	echo ""
        echo "ABC Enterprises - Weekly Pay Calculation Process"
        read -p "Enter Employee Category (C, P or S. 0 to quit): " userInput
    elif [ $userInput != "0" ] # Tell the user they entered the wrong option
    then
	echo ""
       	echo "Sorry unknown option!" 
	echo ""
        echo "ABC Enterprises - Weekly Pay Calculation Process"
        read -p "Enter Employee Category (C, P or S. 0 to quit): " userInput
    fi
done
echo "" # print an empty line to make it easier to read
echo "Thank you, Bye!"

