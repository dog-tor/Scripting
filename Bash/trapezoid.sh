#!/bin/bash
#
# Name: dog-tor
# Prompt the user for trapezoid dimensions and print its area.

# Prompt the user for the values.
read -p "Enter the base a : " base_a
read -p "Enter the base b : " base_b
read -p "Enter the height : " height

# Add base A and B, divide that answer by 2, then multiply it by the height.
addi=$(echo "$base_a+$base_b" | bc -l)
divi=$(echo "$addi/2" | bc -l)
multi=$(echo "$divi*$height" | bc -l)

# Assign the resulting value to a new variable.
answer=$multi

# Print the results and limit the output of the variable to 5 charactes due to trailing zeroes.
echo "Area of the Trapezoid is ${answer:0:5} square units."
