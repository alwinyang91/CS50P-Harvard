# Reads a CSV file using csv.DictReader

import csv

students = []

# note: the csv has keys now!
with open("students2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})  # now, the order of name and home does not matter

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
