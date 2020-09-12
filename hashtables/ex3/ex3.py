def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # First we add our Hash Table
    hash_table = {}

    # Add list to return intersections
    result = []

    # Iterate through each list within the arrays list
    for array in arrays:
        # Iterate through each integer within each given list
        for integer in array:
            # Check if the Hash Table have the current integer
            if integer in hash_table:
                # If so, check if it was added to the result list or not
                if integer in result:
                    pass
                else:
                    # If not add the integer to the result list
                    result.append(integer)
            else:
                # if not add the integer to the Hash Table with the 
                # value of 1 to represent the number of times that integer is shown
                hash_table[integer] = 1

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
