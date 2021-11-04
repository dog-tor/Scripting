#!/bin/bash
#
# Name: dog-tor
# Print numbers using a step-value-loop.

# Declare a counting variable.
counter=0

# Set up step-value-loop from 1-25 in +4 increments.
for i in {1..25..4}
  do
    counter=$i # set count value to $i.
    if [ "$counter" -eq 25 ]
    then
	  echo "$counter" # Don't add the comma if the value is equal to 25.
    else
	  echo -n "$counter, "
    fi
  done

