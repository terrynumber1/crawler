import re

regex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
regex2 = re.compile(r'Tina')

mo1 = regex1.search('Batman and Tina Fey 123-456-7890 12-34-56')
mo2 = regex2.search('Batman and Tina Fey 123-456-7890 12-34-56')

print(mo1.group())
print(mo2.group())

Garrison Mission Manager
Master Plan
