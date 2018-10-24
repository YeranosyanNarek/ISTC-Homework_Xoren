import re

class Text_Match:
    def __init__(self, text):
        self.text = text
    # a followed by zero or more 'b's
    def match_2(self):
        if re.search('ab*', self.text):
            return "Found  a match 'a' followed by zero or more 'b's", re.findall('ab*', self.text)
        else:
            return 'Not matched!'

    # a followed by one or more 'b's
    def match_3(self):
        if re.search('ab+', self.text):
            return "Found  a match 'a' followed by one or more 'b's", re.findall('ab+', self.text)
        else:
            return 'Not matched!'

    # a followed by zero or one 'b'
    def match_4(self):
        if re.search('ab?', self.text):
            return "Found  a match 'a' followed by zero or one 'b'", re.findall('ab?', self.text)
        else:
            return 'Not matched!'

    # a followed by three 'b'
    def match_5(self):
        if re.search('ab{3}', self.text):
            return "Found  a match 'a' followed by three 'b'", re.findall('ab{3}', self.text)
        else:
            return 'Not matched!'

    # a followed by two to three 'b'
    def match_6(self):
        if re.search('ab{2,3}', self.text):
            return "Found  a match a followed by two to three 'b'", re.findall('ab{2,3}', self.text)
        else:
            return 'Not matched!'


text = 'aababbabbbabbbbabbbbb'
p = Text_Match(text)
print(p.match_2())
print(p.match_3())
print(p.match_4())
print(p.match_5())
print(p.match_6())




