def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if a == b:
        return 'Numbers are equal'
    if a > b:
        print('First is greater')
        return f"{a} is more than {b}"
    if b > a:
        print("Second is greater")
        return f"{b} is more than {a}"
    
    # if a > b:
    #     return "First is greater"
    # elif b > a:
    #     return "Second is greater"
    # else:
    #     return "Numbers are equal"