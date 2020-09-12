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
    # Hashtable creates
    hashtable = {}
    # array of string for the route order
    route = []
    # add all of the tickets to the hash table k = source v destination
    for ticket in tickets:
        hashtable[ticket.source] = ticket.destination
    # starting point for the array
    route.append(hashtable['NONE'])

    # Loop through all of the tickets and insert into array in order except the last one because of none.
    for i in range(length - 1):
        if route[i] in hashtable:
            # get the current destination and use it to set the next one by the source
            route.append(hashtable[route[i]])

    return route
