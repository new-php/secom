from constants import char_sets


def match_password(pswd, confirm_pswd):
    if pswd == confirm_pswd and pswd != "":
        return True
    else:
        return False

def eight_chars(pswd):
    if len(pswd) >= 8:
        return True
    else:
        return False

def contains_char(ety_txt, *args):
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
    valid_chars = char_sets.custome_set(*args)

    if not inpset - valid_chars:
        return True
    else:
        return False

def all_filled(info):

    invalid = []

    for item in info:
        if not item[0]: invalid.append(item[1])

    return invalid