def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    hashtable = {}
    # Loop through the list of weights
    for i in range(length):
        # subtract weight from limit
        remaining = limit - weights[i]
        #check to see if the remaining value is in the hashtable
        if remaining in hashtable:
            # set value found in hashtable to output
            output = hashtable[remaining]
            # create the array with the weight and remaining values
            result = [i, output]
            result.sort(reverse=True)
            return result
        else:
            hashtable[weights[i]] = i

    return None
