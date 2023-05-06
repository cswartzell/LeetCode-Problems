# Lets be smart and use combinatronics here. Python does this wonderfully
from collections import defaultdict
from collections import Counter
from math import ceil
import itertools


class Solution:
    def numRollsToTarget(self, n: int, k: int, t: int) -> int:
        Base Case:
        if n == 1 and target <= k:
            return 1

        min_dice = ceil(target/k)
        max_dice = min(n, target)
        #we can ignore combinations including faces above this value
        max_face = min(k, target-n)
        if min_dice > n or max_face < 1:
            return 0




        # aaaaand Im sutck. Well... theres the obvious method: throw them bones.
        # which is an INSANE and impossible thing to do. That'd be O(k^^n)
        # With memoization its not nearly so bad but... the space gets huge for the
        # cache. Also, its still a fuckboat of combinations. Ive got nothing... lets start
        # that. Surely parts of it will be usefull for the less retarded version.

        # CartesianProduct = itertools.product(range(1,min(k+1, target-n+1)),repeat=n)
        # sumsOfProducts = map(sum, CartProduct)
        # CountOfSums = Counter(sumsOfProducts)
        # ans = CountOfSums[target]
        # return ans
        return Counter(
            map(sum, itertools.product(range(1, min(k + 1, t - n + 1)), repeat=n))
        )[t]


test = Solution()
print(test.numRollsToTarget(13, 4, 48))
