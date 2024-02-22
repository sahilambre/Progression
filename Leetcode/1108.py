def defangIPaddr(address):
    new_string = ''
    for char in address:
        if char == ".":
            new_string += "[.]"
        else:
            new_string += char
    return new_string
            