# Uses re.search

import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)  # () can capture str in ()

if matches:
    last, first = matches.groups()  # here is groups() !!!
    name = first + " " + last
print(f"hello, {name}")

'''
python format1.py
Yang, Zewen
'''
