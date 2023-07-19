
# 07-18-2023 Leetcode 146. LRU Cache
# https://leetcode.com/problems/lru-cache/description/

# Classic. So obviously we can implement GET as a simple dict.
# The problem does not explain, does GET reset the timing for the retrieved element?
# I think it typically does. Anyhow, somehow we need to update order IN O(1)
# So we cant search a list and update it. We also cannot cheat and store whether 
# a key val is OUTSIDE some current window as this exceeds the size. We cant 
# increment or decrement EVERY value in some array

# What about a sort of hashed linked list? Each key stores not only its value, but
# the key that proceeded it as well as the key that follows it. 

# In order for this to work we need to keep a few extra pointers: one always points 
# to the Tail, so we can delete this element, modify the next node to be the new tail
# Similarly we keep a pointer to the head. When we perform a put we do one of two things:

#If it is a key ALREADY in our dict, get its PRE and POST. Set the POST of our called nodes
# PRE to our called nodes POST. Similarly for our called nodes POST, set that nodes PRE to 
# our called nodes PRE. We neatly snip out the existing nodem retying the pointers to keep 
# the chain. We then make a new node and adjust the head.

# If the key is new, and our Cache is full we must delete a node. This is just losing the
# TAIL node, and modifying the next node to be the TAIL. Then add our new node to the HEAD
# and modify the existing HEAD to point to it. These are basic linked list operations but
# we imbed them in a dict format so we dont have to traverse the whole list to get to 
# the called node. Easy Peasy right?


# Originally I was going to write some checks for "is the LRU full, if so do this" but that
# seems foolish as the CHECK will always be performed and yet nearly ALWAYS the cache would be
# full. Its only not full briefly after instantiation. I think instead its better to spend a bit
# more time during instantiation to fill the cached with dummy data such that it IS full.
# Now, as we are supposed to return a -1 for value if a node is NOT in the dict, we can use this
# as a safe trick to store CAPACITY number of nodes with the dummy value OF -1. Technically until
# they all fall off via invalidation, running a GET on our dummy list is not failing to find
# a key, value pair and returning a -1 to indicate this but rather IS finding a key value pair
# but the value happens to be our negative indicator. This works in this toy example and could be
# NONE instead of -1 (which actually seems a bit silly, but the reqs say we are only storing positive ints)

# ANNOYING. There is a case where the capacity is one. This means I have to slightly write aroudn my
# dummy data maker. The whole exercise is silly for an LRU of one element. 


class LRUCache:
    def __init__(self, capacity: int):
        # key for LRU is (VALUE, PREV, NEXT)
        # Where PREV and NEXT point to the key proceeding and following this key, respectively
        self.LRU = dict()

        # Fill the LRU with junk data, where the value is -1, which IS the default 
        # and thus if we access the junk before cleared it presents the correct answer
        for i in range(capacity):
            self.LRU[i] = [-1, i-1, i+1]
        
        # Set head and tail pointers and correct their respective PREV and NEXT to None
        self.head = 0
        self.tail = capacity - 1
        self.LRU[self.head][1] = None
        self.LRU[self.tail][2] = None

    def get(self, key: int) -> int:
        if key in self.LRU:
            self.update(key, self.LRU[key][0])
            return self.LRU[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.update(key, value)
    
    def update(self, key: int, value: int) -> None:
        # Special case, key IS already tail. Just update its value
        if key == self.tail:
            self.LRU[key][0] = value
            return
        
        # Either the key doesnt exist so we need to add it (and LRU is ALWAYS full, so delete head)
        # or our element IS the head and we need to update it this way to avoid pointer issues

        #STUPID fix: update the tail FIRST before deleting the head to take care of the one FREAK
        # edge case where the cache is of size one, so deleting the head means there is NO TAIL to update
        self.LRU[self.tail][2] = key
        if key == self.head or key not in self.LRU:
            delete = self.head
            self.head = self.LRU[self.head][2]
            del self.LRU[delete]

        # Key is IN dict, but not at tail nor head, so snip it out
        else:
            self.LRU[self.LRU[key][1]][2] = self.LRU[key][2]
            self.LRU[self.LRU[key][2]][1] = self.LRU[key][1]    

        # Add the key/val to the tail of the list, updating the tail pointer
        self.LRU[key] = [value, self.tail, None]
        self.tail = key
