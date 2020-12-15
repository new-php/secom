import string
from constants import char_sets


def password(pswd, pswd_confirm):
    """
    """

    if eight_chars(pswd) and match_password(pswd, pswd_confirm):
        return True
    else:
        return False

def match_password(pswd, confirm_pswd):
    if pswd == confirm_pswd:
        return True
    else:
        return False

def eight_chars(pswd):
    if len(pswd) >= 8:
        return True
    else:
        return False

def contains_char(ety_txt, constraints):
    """
    INPUT:
        - entry --------> string.
        - contraints ---> string conatingin valid key(s) values for dict
                          `cataloge` in char_sets file.
    OUTPUT:
        - True when entry compplies with constraints.
        - False when entry does not complies with entry.

    DESCRIPTION: Validates if `entry` only contains the CONSTSTAINTS characters.
    """

    inpset = set([letter for letter in ety_txt])
    valid_chars = char_sets.custome_set(constraints)

    if not inpset - valid_chars:
        return True
    else:
        return False

def all_filled(info):

    for item in info:
        if not item:
            return False

    return True