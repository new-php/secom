import string
from constants import char_sets

def parse_info(entries):
    """
    Adds 'error' key to entries with a bool value depending
    on complience with input type.
    """

    for info in entries:
        entries[info]['error'] = confirm_inp(entries[info])

def letters(entry):
    """
    INPUT:
        - string.
    OUTPUT:
        - True when input is a valid char.
        - False when input is not a valid char.

    Description: Validades inputs which only allow LETTERS.
    """

    inpset = set([letter for letter in entry])
    valid_chars = char_sets.ltrs

    if valid_chars.issuperset(inpset):
        return True
    else:
        return False

def letters_numbers(entry):
    """
    INPUT:
        - string.
    OUTPUT:
        - True when input is a valid char.
        - False when input is not a valid char.

    Description: Validades inputs which only allow LETTER and DIGITS.
    """
    inpset = set([letter for letter in entry])
    valid_chars = char_sets.ltrs_nmbrs

    if valid_chars.issuperset(inpset):
        return True
    else:
        return False

def letters_numbers_specials(entry):
    """
    INPUT:
        - string.
    OUTPUT:
        - True when input is a valid char.
        - False when input is not a valid char.

    Description: Validades inputs which only allow LETTERS, NUMBERS and SPECIAL 
                 characters.
    """

    inpset = set([letter for letter in entry])
    valid_chars = char_sets.ltrs_nmbrs_spchars

    if valid_chars.issuperset(inpset):
        return True
    else:
        return False

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

def password(pswd, confirm_pswd):
    """
    IMPUT:
        - string x2.
    OUTPUT:
        - List of boolean values (size 5).

    Description: Validates password such that matchs with 'confirm_pswd' and
    that it contains the following:
        - 8+ characters.
        - Min 1 upper case letter.
        - Min 1 lower case letter.
        - Min 1 special character.
        - Min 1 digit.
    """

    error = []
    
    error.append(eight_chars):


def match_password(pswd, confirm_pswd):
    if pswd == confirm_pswd:
        return False
    else:
        return False

def eight_chars(pswd):
    if len(pswd) < 8:
        return True
    else:
        return False

def right_chars(pswd):
