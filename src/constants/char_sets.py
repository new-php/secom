import string

"""
File contains a dict `cataloge` with sets from which custome sets can be created.
"""

catalogue = {
    'ltrs upper case': set(string.ascii_uppercase),
    'ltrs lower case': set(string.ascii_lowercase),
    'ltrs': set(string.ascii_letters),
    'dgts': set(string.digits),
    'spchars': {'!',
                '@',
                '#',
                '$',
                '%',
                '^',
                '&',
                '*',
                '<',
                '>',
                '?',
                '-',
                '_'
        },
    'space': {' '}
}

def custome_set(*args):
    """
    IMPUT:
        - string(s) found as keys in catalogue.
    OUTPUT:
        - set
    DESCRIPTION: Creates a set with the requirements needed from base sets.
    """
    
    custome = set()

    for item in args:
        custome |= catalogue[item]

    return custome
