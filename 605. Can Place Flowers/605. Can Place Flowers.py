# 03-19-2023 Leetcode 605. Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/description/

# We could do a quick math check, sum the 1s and see if its half the len.
# Not sure it buys us much. Is it enough that we can merely subtract half the
# len to find how many spots remain? STRONGLY suspect we'd get an off by one err

# [0,1,0,1,0] Is a valid bed with just 2 flowers and ZERO additional room
# [1,0,0,0,1] Has two flowers and room for one, so its all good
# [1,0,0,1,0] -> [1,0,0,1]

# I think if we CAN put a flower on the end, we always should. There is no benefit to
# crowding it in. So, check the two ends. After that, we can only add one if there are
# three 000 in a row. We cant just search for these individually though, as 00000->10101
# So I guess sliding window? This seems like a more complicated solution than is normally
# called for. ANNOYED to be stumped on an easy. Well, not stumped, but I dont want to window


# Ok, so IFF the flowerbed is like this: [0,1.....1,0] the trailing zeros do nothing for us.
# CAN we just chop them out of the len of the array, and THEN use the ceiling max flowers trick?
# I suspoect so.





class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # if n == 0:
        #     return True 

        # if len(flowerbed) > 1:
        #     if flowerbed[0] == 0 and flowerbed[1] == 1:
        #         flowerbed  = flowerbed[1:]
        #     if flowerbed[-1] == 0 and flowerbed[-2] == 1:
        #         flowerbed  = flowerbed[:-1]

        # #Bah! it didnt work. My unproven mathy hunch was off.
        # #Not even by one, I think you can only get 15 of 17 asked for flowers here. 
        # # 86 chars, max flowers = 43, curr flowers = 24. 24 + 17 = 41 which is TWO under our maximum, but its not doable after all. 
        # # [0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0]
        # return n <= math.ceil(len(flowerbed)/2) - sum(flowerbed)
            
        
        I guess I concede to my dummy version

        if n == 0:
            return True 
        
        if n > math.ceil(len(flowerbed)/2):
            return False
        
        if len(flowerbed) == 1:
            return flowerbed[0] == 0 and n == 1

        if len(flowerbed) > 1:
            if flowerbed[0] == flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1
            if flowerbed[-1] == flowerbed[-1] == 0:
                flowerbed[-1] = 1
                n -= 1

        #I feel completely stupid doing it this way
        if len(flowerbed) > 2:
            i,j,k = 0, 1, 2
            while k < len(flowerbed) and n > 0:
                if flowerbed[i] == flowerbed[j] == flowerbed[k] == 0:
                    flowerbed[j] = 1
                    n -= 1
                    i += 1
                    j += 1
                    k += 1
                i += 1
                j += 1
                k += 1

        return n <= 0
        