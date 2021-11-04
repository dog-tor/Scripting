#!/usr/bin/python
import time

"""
Name: dog-tor
Print a receipt based on inputed quantities for items.
"""

# Print the title.
print("\tAffordable Daily Needs")
print("This program will prompt for 10 items.")
print("Enter quantity of each item purchased")

# Assign input as float data type to variables.
bread_count = float(input("How many loaves of Bread ($1.50 each): "))
milk_count = float(input("How many gallons of Milk ($2.25 each): "))
chips_count = float(input("How many bags of Chips ($3.60 each): "))
potato_count = float(input("How many pounds of Potatoes ($0.99/lb): "))
banana_count = float(input("How many pounds of Bananas ($0.36/lb): "))
beef_count = float(input("How many pounds of Beef ($3.89/lb): "))
tomato_count = float(input("How many pounds of Tomatoes ($0.89/lb): "))
apple_count = float(input("How many pounds of Apples ($0.69/lb): "))
battery_count = float(input("How many 2-pack AA batteries ($2.29 each): "))
vitamin_count = float(input("How many Vitamin bottles ($4.59 each): "))

# Calculate the cost for each item.
bread_cost = bread_count * 1.5
milk_cost = milk_count * 2.25
chips_cost = chips_count * 3.6
potato_cost = potato_count * .99
banana_cost = banana_count * .36
beef_cost = beef_count * 3.89
tomato_cost = tomato_count * .89
apple_cost = apple_count * .69
battery_cost = battery_count * 2.29
vitamin_cost = vitamin_count * 4.59

# Calculate the subtotal.
sub_total = bread_cost + milk_cost + chips_cost + potato_cost + banana_cost + beef_cost + tomato_cost + apple_cost + battery_cost + vitamin_cost
tax_sub_total = battery_cost + vitamin_cost

# Calculate the total (includes tax).
total = sub_total + (tax_sub_total * .0825)

# Print the receipt header.
print("\n===================================")
print("  Affordable Daily Needs")
print("   2300 N. Loop 1604 E")
print("   San Antonio TX 78258")
print("-----------------------------------")
print("{0:11s} {1:4s} {2:11s} {3:7s}".format("Item","Qty",'price/unit',"cost"))
print("-----------------------------------")

# Print the items.
print("{0:10s} {1:4.1f} {2:7.2f} {3:9.2f}".format("Bread",bread_count,(1.5),bread_cost))
print("{0:10s} {1:4.1f} {2:7.2f} {3:9.2f}".format("Milk",milk_count,(2.25),milk_cost))
print("{0:10s} {1:4.1f} {2:7.2f} {3:9.2f}".format("Chips",chips_count,(3.6),chips_cost))
print("{0:10s} {1:4.1f} {2:7.2f} {3:9.2f}".format("Potatoes",potato_count,(.99),potato_cost))
print("{0:10s} {1:4.1f} {2:7.2f} {3:9.2f}".format("Bananas",banana_count,(.36),banana_cost))
print("{0:10s} {1:4.1f} {2:7.2f} {3:9.2f}".format("Beef",beef_count,(3.89),beef_cost))
print("{0:10s} {1:4.1f} {2:7.2f} {3:9.2f}".format("Tomatoes",tomato_count,(.89),tomato_cost))
print("{0:10s} {1:4.1f} {2:7.2f} {3:9.2f}".format("Apples",apple_count,(.69),apple_cost))
print("{0:10s} {1:4.1f} {2:7.2f} {3:9.2f}".format("Batteries",battery_count,(2.29),battery_cost))
print("{0:10s} {1:4.1f} {2:7.2f} {3:9.2f}".format("Vitamins",vitamin_count,(4.59),vitamin_cost))
print("...................................")

# Print the totals.
print("{0:10s} {1:22,.2f}".format("Sub Total",sub_total))
print("{0:10s} {1:20,.2f}".format("Tax @ 8.25% ",(tax_sub_total * .0825)))
print("-----------------------------------")
print("{0:10s} {1:22,.2f}".format("TOTAL ",total))
print("===================================")

# Print the clerk's name and the date.
print("Sales Clerk: dog-tor")
print("{0:6s}{1:s}".format("Date: ",time.strftime('%m/%d/%Y %H:%M:%S')))
