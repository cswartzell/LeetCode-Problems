# 04-07-2023 Leetcode 443. String Compression
# https://leetcode.com/problems/string-compression/description/

# Lets list the situations when comparing two chars:
# 1) We are NOT currently couting reps:
#    A) Immediate mismatch: no reps, new char:
#    advance all 3 pointers
#
#    B)The two chars match: start counting reps, only
#    move next char. (write_idx == next_char)
#        When a mismatch is discovered, write the count
#        at the write_idx, add to total, advance write_idx, write
#        the next_char at write_idx, prv_ = nxt, advance next

#


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        prv, nxt, write_idx = 0, 1, 1
        rep_count = 0

        # Advance next char pointer through str
        while nxt < len(chars):
            # If we werent tracking duplicates, start doing so now:
            if chars[prv] == chars[nxt] and rep_count == 0:
                rep_count = 1
                # Keep counting duplicates til the end of the str, or a mismatch
                while nxt < len(chars) and chars[prv] == chars[nxt]:
                    rep_count += 1
                    nxt += 1
                # Write in the number of reps in str format, may be multiple chars
                for num_char in str(rep_count):
                    chars[write_idx] = num_char
                    write_idx += 1
                rep_count = 0
                continue
            # Not a match, write in the single char and everything advances
            prv = nxt
            nxt += 1
            chars[write_idx] = chars[prv]
            write_idx += 1

        # write_idx gets advanced to next EXPECTED char to be written, so is NOT zero indexed
        # Therefore, it IS the len of the compressed str
        return write_idx
