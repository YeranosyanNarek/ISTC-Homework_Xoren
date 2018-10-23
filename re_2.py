import re
str1 = 'Being able to match varying sets of characters is the first thing regular' \
       ' expressions can do that isn’t already possible with the methods available ' \
       'on strings. However, if that was the only additional capability of regexes, ' \
       'they wouldn’t be much of an advance. Another capability is that you can specify ' \
       'that portions of the RE must be repeated a certain number of times.'
str2 = 'abbbbbcbbbbdfghijk'

p = re.compile('ab*')
print(re.findall(p, str2))
print('===========')
print(re.findall(p, str1))


