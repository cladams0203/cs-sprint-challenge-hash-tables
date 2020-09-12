def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Create hashtable
    hashtable = {}
    # Create the array for the result
    result =[]
    # loop through all of the arrays and add the numbers hashtable incrementing
    # the value if a duplicate is found
    for i in arrays:
        for j in i:
            if j not in hashtable:
                hashtable[j] = 1
            else:
                hashtable[j] += 1
                if hashtable[j] == len(arrays):
                    result.append(j)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
