import string

"""
File contains customized sets of characters for input validation.
"""

cataloge = {
    'ltrs': set(string.ascii_letters),
    'ltrs_nmbrs' :set(string.digits),
    'ltrs_nmbrs_spchars': {'!', '@', '#', '$', '%', '^', '&', '*', '<', '>', '?'}
}

def custom_set(requirements):
    """
    IMPUT:
        - touple.
    OUTPUT:
        - set
    DESCRIPTION: Creates a set with the requirements needed from base sets.
    """
    
    custome = set()

    for item in requirements:
        custome |= cataloge[item]

    return custome



# set of letters including 'ñ' and 'Ñ'.
ltrs = set(string.ascii_letters)
ltrs |= {'ñ', 'Ñ'}

# set of leters including 'ñ' and 'Ñ' and nomber from 0 to 9.
ltrs_nmbrs = ltrs
ltrs_nmbrs |= set(string.digits)

# set of leters including 'ñ' and 'Ñ' and nomber from 0 to 9.
ltrs_nmbrs_spchars = ltrs_nmbrs
ltrs_nmbrs_spchars |= {'!', '@', '#', '$', '%', '^', '&', '*', '<', '>', '?'}

