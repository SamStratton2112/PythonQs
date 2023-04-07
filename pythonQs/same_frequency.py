#complete
def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1= sorted(str(num1))
    num2= sorted(str(num2))
    num_d1= {}
    num_d2= {}
    for num in num1:
        num_d1[num] = num_d1.get(num,0)+1
    print(num_d1)
    for numm in num2:
        num_d2[numm] =num_d2.get(numm,0)+1
    print(num_d2)
    if num_d1 == num_d2:
        return True
    else:
        return False
