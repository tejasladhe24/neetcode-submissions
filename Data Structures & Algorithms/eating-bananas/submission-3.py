class Solution:
    def checkSpeed(self,piles,h,speed):
        total_time = 0
        for pile in piles:
            total_time += math.ceil(pile / speed)
        
        return total_time <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # speed = 1
        # while True:
        #     ans = self.checkSpeed(piles,h,speed)

        #     if ans:
        #         return speed

        #     speed +=1

        l,r=1,max(piles)
        min_speed = max(piles)

        while l<r:
            curr_speed = (l+r)//2
            ans = self.checkSpeed(piles,h,curr_speed)

            if ans:
                min_speed = min(min_speed, curr_speed)
                r = curr_speed
            else:
                l = curr_speed + 1
        
        return min_speed