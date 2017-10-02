def concatenate_list(a,b):
    """
    concatenates two lists
    """
    a.extend(b)
    return a

if __name__ == '__main__':

    l1 = [2, 3, 5]
    l2 = [7, 8, 9]

    nl = concatenate_list(l1, l2)
    print(nl)



