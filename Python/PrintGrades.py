# Name: dog-tor
# This program will read from the grades_input.dat file, format the grades depending on the preceding array location, then
# it will calculate the grand total, averages, and total ranks for the students.

# Import the grades_input.dat file.
grade_doc = open("grades_input.dat", "r")

# Define arrays.
grade_table = [ [ 0.0 for i in range(6) ] for j in range(15) ]
student_names = [
    'Alice Arnold', 'Cory Brown', 'Sean Douglas', 'Pete Douglas', 
    'Mary Fleming', 'Joel Jacob', 'Jeramy Ghouse', 'Hansie Holder', 
    'Loyola Ingenious', 'Gary Jackson', 'Russell Jacobson', 
    'Dustan Kellart', 'Carl Melone', 'Samuel Peterson', 'Alec Stewart'
    ]

# Define grade counts.
a_count = 0
b_count = 0
c_count = 0
d_count = 0
f_count = 0

# Define column totals.
english_total = 0.0
math_total = 0.0
history_total = 0.0
geography_total = 0.0
science_total = 0.0
programming_total = 0.0
total_total = 0.0

# Print the formatted header.
print("="*87)
print("{:>35s}{:<35s}".format('Developer:', ' dog-tor'))
print("="*87)
print("{:>35s}{:<35s}".format('School Name:', ' Ronald Reagan High School'))
print("{:>35s}{:<35s}".format('Teacher:', ' Mr. Monty Slowashky'))
print("{:>35s}{:<35s}".format('Grade:', ' 10'))
print("{:>35s}{:<35s}".format('Semester/Year:', ' Spring 2021'))
print("="*87)
print("{:<19s}{:<7s}{:<8s}{:<8s}{:<11s}{:<9s}{:<13s}{:<7s}{:<4s}".format('Student Name', 'English ', 'Math', 'History', 'Geography', 'Science', 'Programming', 'Total', 'Rank'))
print("="*87)

# Assign values to grade_table array.
for item in grade_doc:
    item = item.split() # Split the lines/rows in the document.
    row = int(item[0][0:2]) # Row index substring.
    column = int(item[0][2:4]) # Column index substring.
    grade = float(item[1]) # Grade string.
    grade_table[row][column] = grade # Assign values to grade_table array.

# Loop through grade_table array.
for item in range(len(grade_table)):

    # Determine the letter grade rank.
    if sum(grade_table[item]) >= 540.0: # A letter grade.
        rank = 'A'
        a_count += 1
    elif sum(grade_table[item]) >= 480.0 and sum(grade_table[item]) < 540.0: # B letter grade.
        rank = 'B'
        b_count += 1
    elif sum(grade_table[item]) >= 420.0 and sum(grade_table[item]) < 480.0: # C letter grade.
        rank = 'C'
        c_count += 1
    elif sum(grade_table[item]) >= 360.0 and sum(grade_table[item]) < 420.0: # D letter grade.
        rank = 'D'
        d_count += 1
    elif sum(grade_table[item]) < 420.0: # F letter grade.
        rank = 'F'
        f_count += 1
    else: # Fail-safe
        rank = 'N/A'
    
    # Print the formatted table.
    print('{:<16s}{:>8.2f}{:>8.2f}{:>8.2f}{:>9.2f}{:>11.2f}{:>12.2f}{:>9.2f}{:^8s}'.format(student_names[item], *grade_table[item], sum(grade_table[item]), rank))

    # Calculate the column totals.
    english_total += grade_table[item][0]
    math_total += grade_table[item][1]
    history_total += grade_table[item][2]
    geography_total += grade_table[item][3]
    science_total += grade_table[item][4]
    programming_total += grade_table[item][5]
    total_total += sum(grade_table[item])

# Print the footer with statistics.
print("-"*87)
print("{:<16s}{:>8.2f}{:>8.2f}{:>8.2f}{:>9.2f}{:>11.2f}{:>12.2f}{:>9.2f}".format('Grand Totals', english_total, math_total, history_total, geography_total, science_total, programming_total, total_total))
print("-"*87)
print("{:<16s}{:>8.2f}{:>8.2f}{:>8.2f}{:>9.2f}{:>11.2f}{:>12.2f}{:>9.2f}".format('Averages', english_total/15, math_total/15, history_total/15, geography_total/15, science_total/15, programming_total/15, total_total/15))
print("="*87)
print("{:>22s}{:>9s}{:>1d}{:>9s}{:>1d}{:>9s}{:>1d}{:>9s}{:>1d}{:>9s}{:>1d}".format('Ranks', 'A\'s: ', a_count, 'B\'s: ', b_count, 'C\'s: ', c_count, 'D\'s: ', d_count, 'F\'s: ', f_count))
print("="*36+"End of Report"+"="*38)
