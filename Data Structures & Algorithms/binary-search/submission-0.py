class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n-1

        while l<=r:
            mid = (l+r)//2
            val = nums[mid]

            if val == target:
                return mid
            elif val > target:
                r -= 1
            else:
                l += 1
        
        return -1