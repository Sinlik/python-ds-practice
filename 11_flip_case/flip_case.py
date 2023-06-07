def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # if to_swap.isupper():
    #     print("upper")
    #     for char in phrase:
    #         if char.isupper() and char == to_swap:
    #             print(char.lower(), end = "")
    #         if char.islower() and char == to_swap:
    #             print(char.upper(), end = "")
    # if to_swap.islower():
    #     print("lower")
    #     return phrase.upper()
    
    to_swap = to_swap.lower()
    out = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        out += ltr
    return out
