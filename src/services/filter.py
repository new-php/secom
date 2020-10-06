import string

def parse_info(entries):
    """
    Adds 'error' key to entries with a bool value deoending
    on complience with input type.
    """

    for info in entries:
        entries[info]['error'] = confirm_inp(entries[info])


def confirm_inp(inp):
    """
    INPUTS:
    - imp ---> dict (keys: 'value', 'input type')
    OUTPUT:
    - True when input complies with valid characters.
    - False otherwise.

    Description: uses sets to ckeck for invalid chars 
    depending on the input type
    """
    inpset = set(lambda char: char for char in inp['value'])
    valid_chars = set()
                
    # Adds all valid characters to `valid_chars` depending on
    # `innput type `
    for typ in inp['input type']:
        for letter in typ:
            if letter == 'L':
                valid_chars |= set(string.ascii_letters)
                valid_chars |= {'ñ', 'á', 'é', 'í', 'ó', 'ú'}
            elif letter == 'N':
                valid_chars |= set(string.digits)
            else:
                valid_chars |= {'!', '@', '#', '$', '^', '&', '*', '<', '>', '?'}
    
    # Removes all valid characters.
    inpset -= valid_chars

    if inpset:
        return False
    else:
        return True

    
