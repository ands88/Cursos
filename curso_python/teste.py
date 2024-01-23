import sys
import math

# Please note that the second variable named 'inputs' is the list of children
# Please rename the second variable called 'inputs' to avoid errors caused by 2 variables of the same name
# If you do not see 2 variables of the same name as in matter discussed above, DO NOT BOTHER
# Just make sure that you have an array variable that the loop is adding each of the name values to
def last_child_reading (students, paragraphs):
    last_child_index = (paragraphs - 1) % len(students)
    return students[last_child_index]

students = ["Jimmy", "Joan", "Jason"]
paragraphs = (int(input("Number of paragraphs: ")))

nameOfLastStudentReading = last_child_reading(students, paragraphs)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(nameOfLastStudentReading)