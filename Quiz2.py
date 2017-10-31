


def letters_generator():
    current = 'a'
    while current <= 'm' :
        yield current
        current = chr(ord(current)+1)

for letter in letters_generator():
    print(letter)