import re
str1 = 'Narek Yeranosyan 15.11.1987 '
p1 = re.compile('[A-Z]')
p2 = re.compile('[a-z]')
p3 = re.compile('[0-9]')

print(re.findall(p1, str1))
print(re.findall(p2, str1))
print(re.findall(p3, str1))


