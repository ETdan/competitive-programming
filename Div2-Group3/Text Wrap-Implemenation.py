import textwrap

def wrap(string, max_width):
    length = 0
    paragraph = ""
    for letter in string:
        paragraph += letter
        length +=1
        if length == max_width:
            paragraph += "\n"
            length = 0
    return paragraph

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
