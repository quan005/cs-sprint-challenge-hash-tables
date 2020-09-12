#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    hash_table = {}
    route = [None] * length

    # First store all the tickets in the Hash Table where the key is the
    # ticket.source and thew value is the ticket.destination
    for ticket in tickets:
        hash_table[ticket.source] = ticket.destination

    # Create the start destination, which is in the Hash Table at 'NONE'
    # not 'None' btw :-|
    start = hash_table['NONE']

    # Finally, we add each destination to our route list and update our start 
    # position
    for i in range(length):
        route[i] = start
        start = hash_table[start]
        print(start)

        
    return route