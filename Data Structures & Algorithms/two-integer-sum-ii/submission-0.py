class Solution:
    def twoSum(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        i,j=0,n-1

        while i<j:
            curr = nums[i]+nums[j]

            if curr > k:
                j-=1
            elif curr < k:
                i+=1
            else:
                return [i+1,j+1]

        return [0,0]