# Replaces character class with \w

import re

email = input("What's your email? ").strip()

'''
\w means normal word a-zA-Z0-9_
'''
if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
