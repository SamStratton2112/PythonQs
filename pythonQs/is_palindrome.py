# complete
def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    x=0
    y= -1
    phrase = phrase.lower().replace(' ', "")
    while x<len(phrase):
        if phrase[x] == phrase[y]:
            x+=1
            y-=1
            return True
        else:
            return False