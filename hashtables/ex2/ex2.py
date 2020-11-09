#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    Create hashtable so the starting location is key and destination
    is value.
    You will need to link the values to know how to find the next one.
    Something like: "if prev = next return value"
    Start with key "none" end when value = "none"
    """
    # Your code here
    # set up blank hastable
    hashTable = {}
    # have to create a list for linking
    route = []

    # create value within tickets
    for tix in tickets:
        hashTable[tix.source] = tix.destination
        # This value will be the destination

    # This is assiging the first key as none

    location = hashTable["NONE"]
    while location != "NONE":
        # If key is not None, then add a new location
        # To the hashtable
        route.append(location)
        location = hashTable[location]

    route.append("NONE")
    # When value destination reaches none
    # return route
    tix.destination == "NONE"

    return route
