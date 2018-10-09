def letter_counter(STRING):
    STRING = STRING.lower()
    counter = dict()
    for letter in STRING:
        if letter in counter:
            count = counter[letter] + 1
        else:
            count = 1
        counter[letter] = count
    return (counter.items())

def main():
    str_0 = input('')
    inp_str = open(str_0, newline='\n')
    inp_str_read = inp_str.read()
    inp_str_txt = letter_counter(inp_str_read)
    print (inp_str_txt)

if __name__ == '__main__':
    main()




