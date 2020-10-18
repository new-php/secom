import string

# set of letters including 'ñ' and 'Ñ'.
ltrs = set(string.ascii_letters)
ltrs |= {'ñ', 'Ñ'}

# set of leters including 'ñ' and 'Ñ' and nomber from 0 to 9.
ltrs_nmbrs = ltrs
ltrs_nmbrs |= set(string.digits)

# set of leters including 'ñ' and 'Ñ' and nomber from 0 to 9.
ltrs_nmbrs_spchars = ltrs_nmbrs
ltrs_nmbrs_spchars |= {'!', '@', '#', '$', '%', '^', '&', '*', '<', '>', '?'}

