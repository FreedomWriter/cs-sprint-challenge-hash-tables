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
    
    for t in tickets:
        print(t.source, t.destination)
        hash_table[t.source] = t.destination

    route = []
    route.append(hash_table["NONE"])
    begin = hash_table["NONE"]

    for _ in range(0, length-1):
        if begin in hash_table:
            route.append(hash_table[begin])
            begin = hash_table[begin]

    return route

