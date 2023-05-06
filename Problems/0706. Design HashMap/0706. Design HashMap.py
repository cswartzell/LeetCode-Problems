"""04-22-2022 Leetcode 706. Design HashMap"""

# A SUPER basic, quick and dirty way to do it is simply init a list of 10**6 + 1 ints as all -1 value.
# The key would then just be the index of the array. Fast access, fast insertion and deletion.
# Notably this is not really a hash, or is maybe "the trivial hash"
# Absurdly wasteful for a sparse list. I'd like to explore a more robust solution, but it gets
# complicated really quickly, particularly if we are trying to avoid "fancy features".
# For fast search of an initially empty list we could build and search our own BST Tree for instance
# but maybe we can just use built in heapsort for ease. For now maybe I'll start with in between
# and lean on Pythons magic "is in"

# Doing some reading on just how a hashmap actually works. I understood the concept:
# "apply algorithm to generate address of key" but didnt understand fundamentally
# that this does not generate a unique exact address but rather an adress for a
# relatively small bucket. We then iterate through the bucket (or BST search or whatever)
# to find the exact key. Hashing REDUCES the list we need to search,  it does not eliminate it.
# There is a lot of complexity therefore as to "but how many buckets?", and how full they get
# This ALSO dispells me of the seemingly incorrect notion (oft cited?) that hashing access is
# O(1). This depends on how many collisions there are in the space, thus how many keys in the
# bucket right? Or I guess we know how many keys CAN map to the bucket, so the big O assumes
# worst case: The bucket has a key:val pair for every key that COULD map to said bucket, and
# thus searching them is O(1), the size of the bucket rather than say single operation

# Well, this is a slightly more involved one than I thought. The concepts are easy though
# (assuming we use linear search for the buckets). I'm going to basically straight rip
# the answer as I want some practise using OOP and I like how it defines the buckets as a
# class with their methods, then the hashmap as a seperate class that implements these


class Buckets:
    def __init__(self):
        self.bucket = []  # simple list of (key, value) tuples

    def put(self, key, value) -> None:
        # linear search. Good hashing algorithms use BST or other optomized search
        for i, key_val in enumerate(self.bucket):
            if key_val[0] == key:
                self.bucket[i] = (key, value)
                # Balls. Tuples are immutable. Cannot reassign just their value, need to
                # overwrite the whole tuple at the index location. (or remove and add)
                return
        self.bucket.append((key, value))

    def get(self, key) -> int:
        for key_val in self.bucket:
            if key_val[0] == key:
                return key_val[1]
        return -1

    def remove(self, key) -> None:
        # self.put(key, -1) cheeky, but no... It adds a "blank" (key, val) rather than removing it.
        # A LOT faster as insertions and deletions of a list are costly. THATS why these are really
        # done with linked lists? If doubly linked you could binary search them
        for i, key_val in enumerate(self.bucket):
            if key_val[0] == key:
                del self.bucket[i]


class MyHashMap:
    def __init__(self):
        self.mod_val = 2069  # a prime value, thus 2069 buckets, each potentially with 484 collisions
        self.hmap = [Buckets() for i in range(self.mod_val)]

        # Man, I really need to learn how to OOP in Python. Variable decs go here? Privatize?
        # self.dumb_map = [-1]*((10**6)+1)       #LoL, giant list for 1:1 key IS index. Terrible

    def put(self, key: int, value: int) -> None:
        self.hmap[key % self.mod_val].put(key, value)
        # self.dumb_map[key] = value

    def get(self, key: int) -> int:
        return self.hmap[key % self.mod_val].get(key)
        # return self.dumb_map[key]

    def remove(self, key: int) -> None:
        self.hmap[key % self.mod_val].remove(key)
        # self.dumb_map[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
