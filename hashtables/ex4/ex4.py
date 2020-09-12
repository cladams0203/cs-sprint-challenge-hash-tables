def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create hashtable
    hashtable = {}
    # create result array
    result = []
    # loop through and add all negative numbers to the hashtable converting to positive
    for i in a:
        if i < 0:
            hashtable[abs(i)] = i
    # search hashtable for matching key that was converted to positive
    for i in a:
        if i in hashtable:
            result.append(i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
