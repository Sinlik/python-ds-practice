def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    # arr = [phrase[-reverse - 1] for reverse in range(len(phrase))]
    
    # for char in range(len(arr)):
    #     print(f"{arr[char]}", end = '')
    
    return phrase[::-1]