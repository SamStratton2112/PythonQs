# complete
def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
#     for li in list:
#         if li not False:

#     [li if ]

# [do_this if something else do_this for thing in iterable]
    return [val for val in lst if val]