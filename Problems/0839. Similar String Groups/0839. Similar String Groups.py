# 05-01-2023 Leetcode 839. Similar String Groups
# https://leetcode.com/problems/similar-string-groups/

#All words are already same len and are anagrams
#I guess this is a union-find thing but am uncertain. If check if
# a given word is in a certain group it might not be YET, but its possible it
# will as other words are added to the group. We presumably dont want to go O(n**2)...
#Then again, 300*2 isnt too bad


#Because we konw the words are anagrams of eachother, we dont actually have to check 
#if we can swap letters, we know we can. We need only know that the word differ at 
#either 0 or 2 spots. If they differ in two and only two letters, then those letters MUST
# be swappable to become the same word. 

#So I guess we are going to to do a nested for and check all possibilites, and keep track
# of the root sort of like union find

#whats the quickest way to count different letters?


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        wordlen = len(strs[0])
        root = [*range(len(strs))]
        self.groups = len(strs)

        def get_root(x):
            while x != root[x]:
                x = get_root(root[x])
            return x

        def union(x, y):
            root_x = get_root(x)
            root_y = get_root(y)

            if root_x < root_y:
                root[root_y] = root_x
                self.groups -= 1
            if root_y < root_x:
                root[root_x] = root_y
                self.groups -= 1

        def diffs(i, j):
            diffs = 0
            x = 0
            while x < wordlen and diffs < 2:
                diffs += strs[i][x] != strs[j][x]
                x += 1
            return diffs  

        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                # diffs = 0 if strs[i] == strs[j] else sum(strs[i][char] != strs[j][char] for char in range(wordlen))
                diff = 0 if strs[i] == strs[j] else diffs(i,j)
                if diff == 0 or diff == 2:
                    union(i, j)
                    
        # for i in range(len(strs)):
        #     root[i] = get_root(i)
        
        # return len(set(root))
        return self.groups
