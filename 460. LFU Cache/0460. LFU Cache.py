# 01-30-2023 Leetcode 460. LFU Cache
# https://leetcode.com/problems/lfu-cache/description/

# Get and Put need to be O(1) so we are obvioulsy hashing here.
# There is a key and TWO data points: its value, and a counter for
# how often we use the key. Should we store the usage as part of a tuple
# right along with the data? seems weird. Seperate heap?

# We need to track: Key:Val Pairs, num uses/least frequently used
# We dont need to keep a count per se of usage if we instead keep a stack
# The bottom of the stack would be the last used. When a key is used (get OR put)
# it moves to the top of the stack. Oooh! In python dicts are implicitly ordered:
# We can simply delete a key val pair, then add it back to the dict each time, then
# the leftmost entry WOULD be the last used.

# no wait. Its LEAST frequently used, not last used. it may have been a while, but
# it may come up often... hmmm.I suspect LRU is least recently used, which is that.
# Ok, so we can just keep a count as part of the tuple, and update as we go.
# we keep a seperate holder for "LFU" and make comparisons as we go, swapping it
# to the new key if we discover its usage is less than the current LRU.
# Wait, nothing resets the LRU, the usage numbers just keep going up...


# hmm.. I could store the access times as a heap, and thus the least used
# would be atop. It SEEMS that ties for heaps keep the OLDER node atop the newer,
# so that would take care of the LFU tie to pick LRU.
# But then UPDATING the value on say a get() invocation becomes a linear scan of the heap?
# awful.

# Im a little stuck on retaining the info on order of use to continuously note the least
# recent usage of keys with the same count. Clearly going to either store YET ANOTHER
# number, or keep them in an ordered data structure...

# Are you fucking kidding me? The capacity can be zero? Literally what the fuck is the point of that?


class LFUCache:
    def __init__(self, capacity: int):
        self.max_cap = capacity
        self.curr_size = 0
        self.LFU_dict = collections.defaultdict(list)
        # Holy shit... really? Its an ordered hashed set... I guess it makes sense
        self.LFU_LRU_ordered = collections.defaultdict(collections.defaultdict)

    def get(self, key: int) -> int:
        # FUCKING STUPID BASE CASE:
        if self.max_cap == 0:
            return -1
        # see_max_cap = self.max_cap
        # see_curr_size = self.curr_size
        # see_LFU_dict = self.LFU_dict
        # see_LFU_LRU_ordered = self.LFU_LRU_ordered

        if key in self.LFU_dict:
            old_count = self.LFU_dict[key][1]
            self.LFU_dict[key][1] += 1
            # UPDATE LFU
            if len(self.LFU_LRU_ordered[old_count]) == 1:
                del self.LFU_LRU_ordered[old_count]
            else:
                self.LFU_LRU_ordered[old_count].pop(key)
            self.LFU_LRU_ordered[self.LFU_dict[key][1]].update({key: None})
            return self.LFU_dict[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # FUCKING STUPID BASE CASE:
        if self.max_cap == 0:
            return
        # see_max_cap = self.max_cap
        # see_curr_size = self.curr_size
        # see_LFU_dict = self.LFU_dict
        # see_LFU_LRU_ordered = self.LFU_LRU_ordered

        if key in self.LFU_dict:
            self.LFU_dict[key][0] = value
            old_count = self.LFU_dict[key][1]
            self.LFU_dict[key][1] += 1
            if len(self.LFU_LRU_ordered[old_count]) == 1:
                del self.LFU_LRU_ordered[old_count]
            else:
                self.LFU_LRU_ordered[old_count].pop(key)
        else:
            # IF LFU_DICT FULL
            if self.curr_size == self.max_cap:
                # DELETE THE LFU
                min_freq = min(self.LFU_LRU_ordered.keys())
                key_to_del = list(self.LFU_LRU_ordered[min_freq])[0]
                if len(self.LFU_LRU_ordered[min_freq]) == 1:
                    del self.LFU_LRU_ordered[min_freq]
                else:
                    self.LFU_LRU_ordered[min_freq].pop(key_to_del)
                self.LFU_dict.pop(key_to_del)
            self.LFU_dict[key] = [value, 1]
            self.curr_size = min(self.curr_size + 1, self.max_cap)
        # UPDATE LFU
        self.LFU_LRU_ordered[self.LFU_dict[key][1]].update({key: None})


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
