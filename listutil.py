def count_unique(list):
    """Count the number of distinct elements in a list.

    The list can contain any kind of elements, including duplicates and nulls in any order.

    :param list:  list of elements to find distinct elements of
    :return: the number of distinct elements in list

    Examples:
    >>> count_unique(['a','b','b','b','a','c','c'])
    3
    >>> count_unique(['a','a','a','a'])
    1
    >>> count_unique([ ])
    0
    """
    unique = []
    for char in list[::]:
        if char not in unique:
            unique.append(char)
    return len(unique)


def binary_search(list, element):
    """Search element sorted in list by repeatedly dividing search interval in half.
    If the value of the search key is less than the list in the middle of the interval,
    narrow the interval to the lower half. Otherwise narrow it to the upper half.
    Repeatedly check until the value is found or the interval is empty.

    :param list: List of elements to find sorted element
    :param element: The value that we want to check whether it is in the list or not
    :return: The position(index) of element in the list.

    Examples:
    >>> binary_search([2,4,6,1,3],3)
    2
    >>> binary_search([1],2) is None
    True
    >>> binary_search([1,2,3,6,8,4,80],None)
    Traceback (most recent call last):
    '''
    TypeError: Search element must not be none
    """
    list.sort()
    first = 0
    last = len(list) - 1
    count = 0
    if element == None:
        raise TypeError("Search element must not be none")
    while first < last:
        midpoint = (first + last) // 2
        if list[midpoint] == element:
            position = midpoint
            return position
        else:
            if list[midpoint] < element:
                count += 1
                if list[midpoint + count] == element:
                    return midpoint + count
            else:
                count += 1
                if list[midpoint - count] == element:
                    return midpoint - count
