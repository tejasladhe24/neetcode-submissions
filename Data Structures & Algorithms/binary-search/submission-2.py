class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n-1

        while l<=r:
            val = nums[(l+r)//2]

            if val == target:
                return (l+r)//2
            elif val > target:
                r -= 1
            else:
                l += 1
        
        return -1