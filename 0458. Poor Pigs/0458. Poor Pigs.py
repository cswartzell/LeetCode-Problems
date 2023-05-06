# 01-31-2023 Leetcode 458. Poor Pigs
# https://leetcode.com/problems/poor-pigs/description/

# This... kinda seems like a binary search
# I thought you literally couldnt do better than that
# so... height of the binary tree of number of buckets?
# that seems like this would then be an easy problem so
# that cannot be right.

# Ok... I think I have an idea based on FASTER binary search
# 1) Split all remaining buckets into two, and test Left half
# 2) If a pig dies, we know its in that half, repeat.
#   The worst case is then just a binary seach for O(nlogn)
# but we arent searching for the worst case, we are asking
# BEST case
# 3) If a pig DOESNT die, then we know its in the right half
# but we dont need to test the right half of this step itself...
# we just confirmed its somewhere in there just now
# 4) Split that section in half and run a test. If a pig dies
# weve just skipped a step and its in this quarter, otherwise
# its in the other half of this step, or the other half of the
# above step: (we'll need to now binary search 3/8ths of the)
# remaining steps.)
# ASSUME We ALWAYS get a poison bucket (ie, best case), then we
# are jumping through the Binary Search more quickly.
# Is it just O(logn) then? No, thats already WORST case

# Oh wait, we are returning the minimum number of pigs, not tests
# Ok, crazy town.
# wait, do we have infinite pigs? There is exactly one bucket... we
# could just feed each pig one bucket and the death pig is the winner...
# the answer would always be one? I am now very confused.
# Oh, ok. We are returning the minimum number of USED pigs, not dead pigs
# One pig could be used if we had infinite time. We dont.
# What does it mean "minimum number of pigs"? If I reused pigs that dont die
# Do I count them again?

# well, first things first: We can easily determine the max number of tests:
# num_tests = minutesToTest//minutesToDie
# We then need to perform overlapping tests to guarentee a best case
# solution in under num_tests.

# So if Binary Search is the fastest, we just need to divide the num of buckets
# into X binary searches, such that the worst case num of tests for each subsection
# is under the number of allotable tests. That seems pretty basic. best case
# for a binary search is O(logn)

# Presumably the more tests we use, the fewer pigs have to be used as we can reuse
# the same pig/s to do more testing
# Therefore, we always want to do as many tests as is possible

# So if we have 4 tests, there are 4 states per pig per test: ie, we count in base 4

# Poison = 1, non poison = 0
# 0001    0010
# 0100    1000

# 1 pig in 4 tests can test bucket 1, 2, 3, 4, then implicitly 5 (if it never dies)
# Therefore a pig can test num_tests + 1 buckets, in num_test roudns: ie '11' buckets in base (num_tests)
# In 4 tests thats 5 buckets checked, or 11base4 buckets
# 1 pig in 4 tests = 11(base 4) = 4+1 buckets tested.
# 2 pigs in base 4 test 101b4 buckets, 16+1 buckets.
# 3:1000b4 = 64+1
# 4: 10000b4 = 265+1
# 5: 100000b4 = 1024+1


# 01-31-2023: What the actual fuck evil wizard did I used to be? ***IIII**** figured this out?
# ridiculous.


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(
            math.log(buckets, 10) / math.log((minutesToTest / minutesToDie) + 1, 10)
        )
        # return math.ceil(math.log(buckets, ((minutesToTest//minutesToDie))))
