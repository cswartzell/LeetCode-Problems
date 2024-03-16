# 03-15-2024 Leetcode 2468. Split Message Based on Limit
# https://leetcode.com/problems/split-message-based-on-limit/
# Time:80 minutes Challenge: 7/10


# The requirement that it be split into as few parts as possible negates the trivial solution
# of left padding with zeros just to make it easy. 

# Can we do this formulaically? Its not trivial. If the parts are kept to single digits then
# the suffixes each add 6 characters. Once we cross into requiring double digits it gets slightly
# more complicated in that the first NINE sections require 5 chars: "<x/yy>", and the remainder 
# require 7: "xx/yy>". This is constant until we need three digits of sections: then the first nine
# are 7 chars, the next 90 are 8 chars, and the remainder are 9 chars. Aha. And now we have it. 
# The magic interval is 9*10^x.

# If you have have 9 sections, that adds 9^0*5 characters. Thats a max of 45 added characters
# to L, the length of the original string. If L + 45 / limit < 9 then you are good. If not, you
# need to split it into possibly double digit chars. This adds a max of 9*10^0 * 6 + 9*10^1 * 7
# chars. Thats 54 + 630 = 684 added suffix chars. Is L + 684 / Limit < 99? And so forth. 

# Ok, so now we have the maximum number of digits for the number of sections. How do we get the
# actual, exact number of sections? Two methods. A) more math. We know we MUST need all the chars
# for the smaller digits (if we need three digits, then clearly we need <x/yyy> through <100/yyy>
# the previous sections is a fixed amount and the remainder is in an exact multiple of 9 chars)
# That means we figure out the REQUIRED added digits, add those to L, then its just Z * 5+e chars that
# get us under the limit. OR B) Just start slicin'. Again, we know we need the first <x-100/YYY> but 
# we dont know what the YYY will be... so figure it out later. Literally use a placeholder, we are
# safe to do so as we know for certain the LENGTH of the place holder is fixed. Slice the sections,
# fill in the placeholder later. 

# Bah. We have a problem. If the number of chars in the suffix eventually EQUALS or exceeds the length
# of the limit, then there is no way to split the message. We need to check for this. 

class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        L = len(message)
        e = 0 #suffix exponent: NUMBER OF DIGITS - 1
        while True:
            if 3 + 2*(e+1) >= limit:
                return []

            suffix_max_total = 0
            for x in range(e+1):
                suffix_max_total += 9*(10**x) * (5+e+x)

            if (L + suffix_max_total) / limit <= 10**(e+1) - 1:
                break
            
            e += 1

        remaining_chars = L
        num_parts = 10**e - 1
        for i in range(1, e+1):
            suffix_len = 3 + i + 1 + e
            remaining_chars -= 9*10**(i-1) * (limit - suffix_len)
        num_parts += math.ceil(remaining_chars / (limit - (3 + 2*(e+1))) )

        E = "/" + str(num_parts) + ">"

        parts = []
        idx = 0
        for part in range(1, num_parts):
            len_message_part = limit - (3 + e+1 + len(str(part)))
            parts.append(message[idx:idx+len_message_part] + "<" + str(part) + E)
            idx += len_message_part
        parts.append(message[idx:] + "<" + str(num_parts) + E)

        return parts
