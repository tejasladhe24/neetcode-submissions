class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        curr,max_area = 0,0

        while l<r:
            length = min(nums[l],nums[r])
            width = r-l
            curr = length*width
            max_area = max(curr,max_area)

            if nums[l]<nums[r]:
                l+=1
            else:
                r-=1
        
        return max_area