def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    evens = 1
    for val in nums:
        if val % 2 == 0:
            evens = evens * val
    return evens

#   to_swap = to_swap.lower()
    # out = ""

    # for ltr in phrase:
    #     if ltr.lower() == to_swap:
    #         ltr = ltr.swapcase()
    #     out += ltr

    # return out