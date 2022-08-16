import re

# find all substrings of 2 characters starting with "a" followed by a character except "b"
for match in re.finditer(r'a[^b]{1}', 'aabacada'):
   print(match.span())


