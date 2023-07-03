# 07-01-2023 Leetcode 2305. Fair Distribution of Cookies
# https://leetcode.com/problems/fair-distribution-of-cookies/description/

# Take it or dont? Can this be calculated empirically or do we need
# to generate ALL the combinations?

# If there are len(cookies) bags to distribute to up to k kids, there are
# k**len(cookies) distributions. In both cases, limited to JUST 8.
# Worst case is 8**8 = 16million. So, calculable? Suspiciously low. 

# I THINK we can do a binary flag kinda thing, XORing out distributions
# but it seems really complicated.

# Wait... Am I an idiot? Is it just a doubly nested loop?
# No, you really do need to distribute ALL the cookies

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def distribute( sums: List[int], next_bag: int, kids_without_cookies: int) -> int:
            #Out of bags, retrurn unfairness
            #Equal or less than bags to distribute then number of kids who havent got one:
            # IE distribute all remaining bags 1:1 for remaining children
            if len(cookies) - next_bag <= kids_without_cookies:
                return max(max(sums) if sums else 0, max(cookies[next_bag:]) if len(cookies) != next_bag else 0)

            min_unfairness = math.inf
            for i in range(k):
                if sums[i] == 0:
                    kids_without_cookies -= 1
                sums[i] += cookies[next_bag]
                min_unfairness = min(min_unfairness, distribute(sums[::], next_bag + 1, kids_without_cookies))
                sums[i] -= cookies[next_bag]
                if sums[i] == 0:
                    kids_without_cookies += 1
            return min_unfairness

        cookies.sort(reverse = True)
        return distribute( [0 for _ in range(k)], 0, k)



       