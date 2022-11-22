        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead
        """     
        
        shownums = nums[:]         #just to hold original nums at the top of the debugger
        
        #so Im too dumb to figure out the number of cycles.
        #wait, holy shit. I was looking at odd numbers and noticed that when len(nums) = 3,5, or 7 the number of cycles was always 1
        #so at first I thought it was just the odds, but of course that doesnt work with 9, as there are cycles of 3. Three of 
        #them specifically. What do 3,5, and 7 have in common? They are prime. Meaning their gcd with any k is 1. But gcd(9, 3) = 3
        # maybe the number of cycles is gcd? It fits all the hand drawn possibilities I have len(nums), k i have from 1-9:1-9
        
        #cycles = math.gcd(n,k) it doesnt see gcd as a part of the math class?
        def getgcd(a,b):                              #blatantly stole this without really looking through it. math.gcd should have worked
            if(b==0):                                 #recursive gcd function  
                return a
            else:
                return getgcd(b,a%b)
        
        cycles = getgcd(k, len(nums))
        
        head = 0        
        while head < cycles:                                   #itr through each CYCLE
            current_i, temp = head, nums[head]        #init each CYCLE head, swap vals
            while True:                                     #loop until CYCLE returns
                next_i = (current_i + k) % len(nums)        #next index
                nums[next_i], temp = temp, nums[next_i]     #sneaky python swap next with temp val, simultaneously storing new temp
                current_i = next_i                          #update position in cycle
                if current_i == head:                      #did cycle loop?
                    break
            head += 1                                      
        
#         while i < len(nums):
#             nums[(i + k) % len(nums)] = temp1
#             i = (i + k) % len(nums) * ((i + k) / abs(i + k))
#                                       #a stupid error since python modulo does not return negative numbers. 
#                                       #Numpy suggestions, or importing other modules. I guess ill just write a cludge
                                        #Oh wait, this was to account for negative k, but the prompt explicitly states k > 0
#             temp1 = temp2
#             temp2 = nums[(i + k) % len(nums)]
#             if i == start:
#                 break
#nope... this results in process a single cyclical pass. This does NOT guarentee a cycle covers the whole loop. Need to use this to process each subcycle by iterating
#... but how many cycles? Obviously a relation between len(nums) and k but what...
                