import string

"""
File contains a dict `cataloge` with sets from which custome sets can be created.
"""

catalogue = {
    'ltrs upper case': set(string.ascii_uppercase),
    'ltrs lower case': set(string.ascii_lowercase),
    'ltr': set(string.ascii_letters),
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
    }
}

def custome_set(requirements):
    """
    IMPUT:
        - touple.
    OUTPUT:
        - set
    DESCRIPTION: Creates a set with the requirements needed from base sets.
    """
    
    custome = set()

    for item in requirements:
        custome |= catalogue[item]

    return custome
