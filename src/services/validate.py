import string
from constants import char_sets

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
    valid_chars = char_sets.custome_set(["ltrs"])

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
    valid_chars = char_sets.custome_set(['ltrs', 'dgts'])

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
    valid_chars = char_sets.custome_set(['ltrs', 'dgts', 'spchars'])

    if valid_chars.issuperset(inpset):
        return True
    else:
        return False

def password(pswd, confirm_pswd):
    """
    IMPUT:
        - string x2.
    OUTPUT:
        - tuple of booleans (size 6).

    Description: Validates password such that matchs with 'confirm_pswd' and
    that it contains the following:
        - 8+ characters.
        - Min 1 upper case letter.
        - Min 1 lower case letter.
        - Min 1 special character.
        - Min 1 digit.
    """

    requirements = ['ltrs upper case', 'ltrs lower case', 'spchars', 'dgts']

    eight_chars(pswd)

    for item in requirements:
        contains_char(pswd, [item])

    match_password(pswd, confirm_pswd)

def match_password(pswd, confirm_pswd):
    if pswd == confirm_pswd:
        return True
    else:
        raise ValueError("password does not match with its confirmation.")

def eight_chars(pswd):
    if len(pswd) >= 8:
        return True
    else:
        raise ValueError("password length is less than 8 characters")

def contains_char(pswd, constraints):
    """
    INPUT:
        - entry --------> string.
        - contraints ---> touple conatingin valid key(s) values for dict
                          `cataloge` in char_sets file.
    OUTPUT:
        - True when entry compplies with constraints.
        - False when entry does not complies with entry.

    DESCRIPTION: Validates if `entry` only contains the CONSTSTAINTS characters.
    """

    inpset = set([letter for letter in pswd])
    valid_chars = char_sets.custome_set(constraints)

    if not valid_chars.isdisjoint(inpset):
        return True
    else:
        raise ValueError("password is not made out of all char types needed.")

def filled(info):
    pass