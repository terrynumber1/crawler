import re

file = open('regex_sum_42.txt', 'r')
print(file.read())

reg1 = re.compile('\\d+')
reg1.findall(file)
