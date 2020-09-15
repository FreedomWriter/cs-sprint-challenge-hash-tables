# #  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP","SLC", "PIT", "ORD", "NONE"]

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    hash_table = {}
    
    # create entries in hash_table where the starting point is the key and the destination is the value
    for t in tickets:
        hash_table[t.source] = t.destination

    route = []
    # add the first flight to the route by checking for the entry where the starting point is "NONE"
    route.append(hash_table["NONE"])
    # give ourselves a pointer to use to find the next flight in our trip
    begin = hash_table["NONE"]

    # loop the appropriate number of times to create a list of the expected length
    for _ in range(0, length-1):
        if begin in hash_table:
            route.append(hash_table[begin])
            # change the value of begin so that it points to the next starting point in the sequence
            begin = hash_table[begin]

    return route

