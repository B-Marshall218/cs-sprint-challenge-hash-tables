def intersection(arrays):
    """
    YOUR CODE HERE

    """
    # temp = set(arrays)
    # result = [value for value in arrays if value in temp]
    # Your code here
    HT = {

    }
    result = []

    # Initialize the array and assign first element
    for e in arrays[0]:
        if e not in HT.keys():
            HT[e] = 1
    # creating capactiy of array
    for i in range(1, len(arrays)):
        for e in arrays[i]:
            # if the element exists and its a key
            # add it and move to the next element
            if e in HT.keys():
                HT[e] += 1
    # check to see if the numbers appear in sub-arrays
    for num1, num2 in HT.items():
        if num2 == len(arrays):
            result.append(num1)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
