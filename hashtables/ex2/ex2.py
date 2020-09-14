# #  Hint:  You may not need all of these.  Remove the unused functions.
# class Ticket:
#     def __init__(self, source, destination):
#         self.source = source
#         self.destination = destination

# expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP","SLC", "PIT", "ORD", "NONE"]

# def reconstruct_trip(tickets, length):
#     """
#     YOUR CODE HERE
#     """
#     # Your code here
#     print(tickets)
#     hash_table = {}
#     for t in tickets:
#         print(t.source, t.destination)
#         hash_table[t.source] = t.destination
#     route = hash_table.values()
#     print(f"expected: {expected}")
#     # return route
#     print(f"hash_table: {hash_table}")
#     print(f"route: {route}")
#  Hint:  You may not need all of these.  Remove the unused functions.
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

# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]

# ticket_1 = Ticket("PIT", "ORD")
# ticket_2 = Ticket("XNA", "SAP")
# ticket_3 = Ticket("SFO", "BHM")
# ticket_4 = Ticket("FLG", "XNA")
# ticket_5 = Ticket("NONE", "LAX")
# ticket_6 = Ticket("LAX", "SFO")
# ticket_7 = Ticket("SAP", "SLC")
# ticket_8 = Ticket("ORD", "NONE")
# ticket_9 = Ticket("SLC", "PIT")
# ticket_10 = Ticket("BHM", "FLG")

# tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
#             ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

# # ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP","SLC", "PIT", "ORD", "NONE"]

# # expected = ["PDX", "DCA", "NONE"]
# result = reconstruct_trip(tickets, 10)
# print(result)