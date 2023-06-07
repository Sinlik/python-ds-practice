def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
#     cap_word = []
#     for char in phrase:
#         cap_word.append(char)
#     cap_word[0] = cap_word[0].upper()

#     return cap_word

# phrase = 'hello world'
# result = capitalize(phrase)
# print(''.join(result))

    return phrase.capitalize()