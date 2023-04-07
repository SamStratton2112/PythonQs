# complete
def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    # return_keys= []
    # prev_key_min= d[1]
    # prev_key_max=d[1]
    # for key in d:
    #     if key< prev_key_min:
    #         prev_key_min = key
    #     return_keys.append(prev_key_min)
    # for key in d:
    #     if key > prev_key_max:
    #         prev_key_max = key
    #     return_keys.append(prev_key_max)
    # return tuple(return_keys)
    keys = d.keys()

    return (min(keys), max(keys))