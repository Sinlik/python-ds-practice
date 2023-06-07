def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    # what I did
    last_num = 0
    if len(lst) < 1:
        print("is None true")
        return None
    
    for val in lst:
        last_num = val
    return last_num

    # proper way
    # if(lst):
    #     return lst[-1]
