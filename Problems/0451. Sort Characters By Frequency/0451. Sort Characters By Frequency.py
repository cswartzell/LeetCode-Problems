#two counters? One just reverses the keys and vals
#so we can sort the vals than reference back the keys?
#Thats dumb right? Ok, Counter first, convert to list of
#tuples, sort tuples, list comp to convert tuples to simple
#list of keys, join those?

#Oh wow, the item*num operator "repeat the previous item num times"
#can be used in our list comprehension to repeat the letters correctly,
#based on the frequency returned in our tuple. Dope

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([x*y for (x, y) in Counter(s).most_common()])
        