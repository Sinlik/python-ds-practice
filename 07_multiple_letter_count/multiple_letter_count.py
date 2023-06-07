def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # unique_ltr = []
    # letters = [ltr for ltr in phrase]
    # previous_ltr = []
    # unique_ltr.append(letters[0])
    # add_ltr = False
    # for i, ltr in enumerate(letters):
    #     if i > 0:
    #         previous_ltr.append(letters[i])
    #         print(f"""letter = {ltr} previous_ltr = {previous_ltr} """)
    # for acum in range(len(previous_ltr)):
    #     add_ltr = False
    #     print(f"add_ltr = {add_ltr}")
    #     if ltr != previous_ltr[acum]:
    #         add_ltr = True
    #         print(f"{ltr} is not {previous_ltr[acum]} add_ltr = {add_ltr}")
    #     if add_ltr == True:
    #         unique_ltr.append(ltr)
    #     # unique_ltr.append(ltr)
    #     # for u_ltr in unique_ltr:
    #     #     if u_ltr == ltr:
    #     #         print("Repeate")
    # return unique_ltr

    counter = {}

    for ltr in phrase:
        counter[ltr] = counter.get(ltr, 0) + 1

    return counter