def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    create hashtable and empy array
    store each weight as key and weights list ht as value
    compare sum of two items at a time to equal weight limit. 
    if it = weight limit return, if it doesn't go to next element. 
    """
    # Your code here
    ht = {}

    for i in range(len(weights)):
        # return items in container
        if limit - weights[i] in ht:
            # if item passed in is subtracted
            return [i, ht[limit-weights[i]]]
            # return the item and the sum
        else:
            ht[weights[i]] = i
            # otherwise return the correct weight pair
            print(i)
    return None
