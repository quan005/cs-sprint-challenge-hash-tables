def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Create a Hash Table to store remaining weight differences
    hash_table = {}

    # Check to see if there are less than 2 values in the weights list, if so
    # return None
    if len(weights) <= 1:
        return None

    # Iterate through the length of the weights list
    for i in range(len(weights)):
        # keep track of the current weight index
        current_weight = weights[i]

        # Check if the current weight is one of the remaining weight differences
        # in the Hash Table.
        if current_weight in hash_table:

            # If so, return a tuple with the index and the current weight from
            # the Hash Table
            return (i, hash_table[current_weight])

        # If not find the remaining weight difference and store it in the 
        # Hash Table
        remaining_weight = limit - weights[i]
        hash_table[remaining_weight] = i

    # If nothing is found then return None
    return None
