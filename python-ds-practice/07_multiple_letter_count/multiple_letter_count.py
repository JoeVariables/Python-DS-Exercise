from calendar import leapdays


def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    
    letter_ctr =  {letter :0 for letter in phrase }
    for letter in phrase:
        letter_ctr[letter]+= 1
        return letter_ctr
    
    