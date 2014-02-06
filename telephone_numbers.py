import re

def get_telephone_numbers(s):
    """ 
    Parses a string with a telephone number to get only the area code,
        the sub area code and the rest of the number.
    
    Returns: A tuple of strings.
    """
    
    numbers = get_phone_numbers(s)
    if not numbers:
        # This condition is for the case when people write the number in
        #     groups of 2 instead of 3 (e.g. '200 12 34 56' instead of
        #     '200 123 456')
        numbers = get_phone_numbers_2(s)
    return numbers

def get_phone_numbers(s):
    regex = r"""
        ^           # Start of the string
        \D*         # Potential trash
        (\d{2,3})   # 2 or 3 digits area code
        \D*         # Optional separator of any number of non-digits
        (\d{3})     # 3 digits sub area code
        \D*         # Optional separator
        (\d{3})     # Rest of number is 3 digits
        \D*         # Potencial trash
        $           # End of the string
        """
    pattern = re.compile(regex, re.VERBOSE)
    
    match = pattern.search(s)
    if match:
        return match.groups()
    else:
        return ()

def get_phone_numbers_2(s):
    regex = r"""
        ^
        \D*
        (\d{2,3})
        \D*
        (\d{2})
        \D*
        (\d{2})
        \D*
        (\d{2})
        \D*
        $
        """
    pattern = re.compile(regex, re.VERBOSE)
    
    match = pattern.search(s)
    if match:
        groups = match.groups()
        s = "".join(groups)             # make a string with all the numbers
        return get_phone_numbers(s)     # parse it to get the desired groups
    else:
        return ()