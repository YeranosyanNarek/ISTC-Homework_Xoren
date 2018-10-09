import sys

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

    inp_str = open(sys.argv[1], newline='\n')
    inp_str_read = inp_str.read()
    inp_str_txt = letter_counter(inp_str_read)
    print (inp_str_txt)

if __name__ == '__main__':
    main()




