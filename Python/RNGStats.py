# Name: dog-tor
# This program will generate a list of 1000 numbers which will be
# used to calculate and print a statistics table.

# Import the random library for random number generation.
import random
# Import statistics library to calculate statistics for the list.
import statistics

# Create the empty variables.
list = []
evens = 0
odds = 0
q1 = 0
q2 = 0
q3 = 0
q4 = 0

# Print the header.
print("-------------------------------------------------")
print("Statistics of Randomly generated 1000 Number List")
print("Developer: dog-tor".center(50))
print("-------------------------------------------------")

# Generate the list numbers, and add them to the list using a loop.
for i in range(1000):
    nextRand = random.randint(1,100)
    list.append(nextRand)

# Print the first set of statistics.
print("List has", len(list), "elements.")
print("Sum of all elements in list is:", sum(list))
print("List has a Maximum value of", max(list))
print("List has a Minimum value of", min(list))
print("Mean of", len(list), "elements in the list is:", statistics.mean(list))
print("Median of", len(list), "elements in the list is:", statistics.median(list)) # No need to sort since the method handles this operation.

# Check if the number is even or odd.
for num in list:   
    if num % 2 == 0: # Even
        evens+= +1
    else: # Odd
        odds+= + 1

# Print the even/odd statistics.
print("List has", evens, "even elements.")
print("List has", odds, "odd elements.")

# Evaluate the element range count.
for num in list:   
    if num > 0 and num <= 25: # 1-25 range
        q1+= 1
    elif num > 25 and num <= 50: # 26-50 range
        q2+= 1
    elif num > 50 and num <= 75: # 51-75 range
        q3+= 1
    elif num > 75 and num <= 100: # 76-100 range
        q4+= 1
    else:
        print("Error. Cannot evaluate range count.")

# Print the range count statistics.
print("List has", q1, "elements between 1 and 25.")
print("List has", q2, "elements between 26 and 50.")
print("List has", q3, "elements between 51 and 75.")
print("List has", q4, "elements between 76 and 100.")
print("-------------------------------------------------")
