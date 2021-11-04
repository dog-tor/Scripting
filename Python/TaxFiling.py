# Name: dog-tor
# This program will prompt for a tax filing status and taxable income,
# then print the calculated income tax to the console.

# Create a variable to hold the tax information
income_tax = 0.0

# Print Header
print("Personal Income Tax Calculator".center(55))
print("Valid Filing Statuses (0 = Unmarried Filer, 1 = Married Filing")
print("Jointly, 2 = Head of Household)\n")

# Assign input to a number for further processing below.
choice = int(input("Enter the filing status: "))
income = float(input("Enter your taxable income: "))

# Choice 0
if choice == 0 and income >= 0 and income <= 9951:
    income_tax = (income * 0.1)
elif choice == 0 and income > 9951 and income <= 40526:
    income_tax = (9951 * 0.1) + ((income - 9951) * 0.12)
elif choice == 0 and income > 40526 and income <= 86376:
    income_tax = (9951 * 0.1) + ((40526 - 9951) * 0.12) + ((income - 40526) * 0.22)
elif choice == 0 and income > 86376 and income <= 164926:
    income_tax = (9951 * 0.1) + ((40526 - 9951) * 0.12) + ((86376 - 40526) * 0.22) + ((income - 86376) * 0.24)
elif choice == 0 and income > 164926 and income <= 209426:
    income_tax = (9951 * 0.1) + ((40526 - 9951) * 0.12) + ((86376 - 40526) * 0.22) + ((164926 - 86376) * 0.24) + ((income - 164926) * 0.32)
elif choice == 0 and income > 209426 and income <= 523601:
    income_tax = (9951 * 0.1) + ((40526 - 9951) * 0.12) + ((86376 - 40526) * 0.22) + ((164926 - 86376) * 0.24) + ((209426 - 164926) * 0.32) + ((income - 209426 )* 0.35)
elif choice == 0 and income > 523601:
    income_tax = (9951 * 0.1) + ((40526 - 9951) * 0.12) + ((86376 - 40526) * 0.22) + ((164926 - 86376) * 0.24) + ((209426 - 164926) * 0.32) + ((523601 - 209426 )* 0.35) + ((income - 523601) * 0.37)

# Choice 1
elif choice == 1 and income >= 0 and income <= 19901:
    income_tax = (income * 0.1)
elif choice == 1 and income > 19901 and income <= 81501:
    income_tax = (19901 * 0.1) + ((income - 19901) * 0.12)
elif choice == 1 and income > 81501 and income <= 172751:
    income_tax = (19901 * 0.1) + ((81501 - 19901) * 0.12) + ((income - 81501) * 0.22)
elif choice == 1 and income > 172751 and income <= 329851:
    income_tax = (19901 * 0.1) + ((81501 - 19901) * 0.12) + ((172751 - 81501) * 0.22) + ((income - 172751) * 0.24)
elif choice == 1 and income > 329851 and income <= 418851:
    income_tax = (19901 * 0.1) + ((81501 - 19901) * 0.12) + ((172751 - 81501) * 0.22) + ((329851 - 172751) * 0.24) + ((income - 329851) * 0.32)
elif choice == 1 and income > 418851 and income <= 628301:
    income_tax = (19901 * 0.1) + ((81501 - 19901) * 0.12) + ((172751 - 81501) * 0.22) + ((329851 - 172751) * 0.24) + ((418851 - 329851) * 0.32) + ((income - 418851 )* 0.35)
elif choice == 1 and income > 628301:
    income_tax = (19901 * 0.1) + ((81501 - 19901) * 0.12) + ((172751 - 81501) * 0.22) + ((329851 - 172751) * 0.24) + ((418851 - 329851) * 0.32) + ((628301 - 418851 )* 0.35) + ((income - 628301) * 0.37)

# Choice 2
elif choice == 2 and income >= 0 and income <= 14201:
    income_tax = (income * 0.1)
elif choice == 2 and income > 14201 and income <= 54201:
    income_tax = (14201 * 0.1) + ((income - 14201) * 0.12)
elif choice == 2 and income > 54201 and income <= 86351:
    income_tax = (14201 * 0.1) + ((54201 - 14201) * 0.12) + ((income - 54201) * 0.22)
elif choice == 2 and income > 86351 and income <= 164926:
    income_tax = (14201 * 0.1) + ((54201 - 14201) * 0.12) + ((86351 - 54201) * 0.22) + ((income - 86351) * 0.24)
elif choice == 2 and income > 164926 and income <= 209426:
    income_tax = (14201 * 0.1) + ((54201 - 14201) * 0.12) + ((86351 - 54201) * 0.22) + ((164926 - 86351) * 0.24) + ((income - 164926) * 0.32)
elif choice == 2 and income > 209426 and income <= 523601:
    income_tax = (14201 * 0.1) + ((54201 - 14201) * 0.12) + ((86351 - 54201) * 0.22) + ((164926 - 86351) * 0.24) + ((209426 - 164926) * 0.32) + ((income - 209426 )* 0.35)
elif choice == 2 and income > 523601:
    income_tax = (14201 * 0.1) + ((54201 - 14201) * 0.12) + ((86351 - 54201) * 0.22) + ((164926 - 86351) * 0.24) + ((209426 - 164926) * 0.32) + ((523601 - 209426 )* 0.35) + ((income - 523601) * 0.37)

else: # Print the error.
    print("Input error in filing Status or income. Processing stopped")

# Print the calculated income tax.
if choice >= 0 and choice <= 2:
    print("Your income tax for 2021 will be: ${:.2f}".format(income_tax))
