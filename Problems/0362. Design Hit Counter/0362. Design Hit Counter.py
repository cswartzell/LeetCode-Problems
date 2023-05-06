# 05-01-2023 Leetcode 362. Design Hit Counter
# https://leetcode.com/problems/design-hit-counter/description/

# just a deque? Popleft when newest hit is more 300+ seconds later?
# Get is just return len dequeue.

# The "only" Issue I see is a space one. How fast can the hits come?
# I dont think there is really any other option.
# Ugh... I guess several hits can occur within a one second span and instead
# of counting a bunch of individual hits, we can just record this into a bucket
# and toss the whole bucket out. NOW we need to keep track of the sums of buckets
# and subtract the whole bucket in one go. Now there can only be 300 buckets, and the
# buckets are just key:val pairs. The timestamps can get pretty big but, oh well.

# Can we make it circular? What if its like a circular prefix sum? just subtract the bucket
# you are about to overwrite? Ok, I think that is brilliant and works, but thats not how
# the ACTUAL PROMPT works. It wants to ask about a timestamp given an int as input. Lame

# What I really want is a sorted dict, becuase I need a key:val pair and also the keys
# are sorted and indexed.

# Deque is close, as the index is the key. But then we need to copy things forward...

# OR we could keep a dict of hits per timestamp and not worry about how many total entries there
# are, thus possibly having less entries. To find the current amount of hits wed binary seach
# on the key, which is the timestamp. This makes the GET operation slower, but the HIT operation
# faster. Sort of. We need to delete records as they get out of date, so now we have to search on those
# See, this is why i want an ordered dict. If the dict itself was a deque we could just peek and pop
# the keys that are older than 300 seconds. I suppose we can do this with two structures. A deque of
# timestamps that ARE the keys to the dict. Count hits in the dict per timestamp, pop records from
# the dict and deque that expire using the deque method. Binary search the deque for the GET op.


# We could FOREVER count up, and then just keep an exipred "hits to subtract" value that removes all
# hits older than 300 seconds from our ever growing list. This actually improves the circular queue


# IM AN IDIOT. This problem works different than I thought. First, theres only up to 300 calls, so few.
# Second, the get timestamp can be from ANY time, so we need to keep the WHOLE record. This actully
# simplifies the whole problem. Just keep a dict form of prefix sum. Each new timestamp is initialized
# to the total of the last time stamp. This is valid because getting a later timestamp permanently freezes
# prior ones. We then add to this. On a get command we simply perform TWO binary searches. One for the
# sought out timestamp (so, recorded_time equal to or LESS than the sought time), which is ALL hits up
# to that point. We then search for the same timestamp -300, and subtract the recorded amount for this
# second time, which is of course all hits OLDER than 300 seconds. Done.

# Jesus its eaven easier. Just keep a total of hits and on each hit update the dict with that amount


# Wow... bottom 13%. Ah well, I think this is quite good. We store literally the minimum amount of info:
# We can check the timestamp for ANY time, so we need to store the total for any given time and this
# does so as minimally as possible. We then perform an efficient search to find the total and expired
# hits for any given timecode, 0-inf.

# class HitCounter:

#     def __init__(self):
#         self.hits = {0: 0}
#         self.total = 0

#     def hit(self, timestamp: int) -> None:
#         self.total += 1
#         self.hits[timestamp] = self.total

#     def getHits(self, timestamp: int) -> int:
#         # keys = list(self.hits.keys())
#         # total_at_t = max(0, bisect.bisect_left(keys, timestamp) - int(timestamp not in self.hits))
#         # expired = max(0, bisect.bisect_left(keys, timestamp - 300) - int(timestamp - 300 not in self.hits))
#         # return self.hits[keys[total_at_t]] - self.hits[keys[expired]]

#         #uglier, but forgos binary search if we can directly access the total at a given time, time -300
#         keys = list(self.hits.keys())
#         total_at_t = self.hits[keys[max(0, bisect.bisect_left(keys, timestamp) - 1)]] if timestamp not in self.hits else self.hits[timestamp]
#         expired = self.hits[keys[max(0, bisect.bisect_left(keys, timestamp - 300) - 1)]] if timestamp - 300 not in self.hits else self.hits[timestamp - 300]
#         return total_at_t - expired


class HitCounter:
    def __init__(self):
        self.times = collections.deque()
        self.hits = collections.defaultdict()
        self.total = 0
        self.last_time = 0  # off by one?

    def hit(self, timestamp: int) -> None:
        expired = 0

        if time_stamp > self.last_time + 300:
            while self.times and self.times[0] < timestamp - 300:
                expired += self.hits[self.times[0]]
                del self.hits[self.times[0]]
                self.times.popleft()

            self.times.append(timestamp)
            self.last_time = self.times[0]

        self.total += 1 - exipired
        hits[timestamp] = total

    def getHits(self, timestamp: int) -> int:
        # ans = self.hits[bisect.bisect_left(self.times, timestamp)]
        return self.hits[self.times[-1]]


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
