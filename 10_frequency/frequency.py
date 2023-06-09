def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    counter = 0

    for val in lst:
        if search_term == val:
            counter += 1
            
    if counter > 0:
        print(f"{search_term} exsits!")
    else:
        print(f"{search_term} doesn't exist")

    return counter

    # return lst.count(search_term)