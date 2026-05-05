class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i,num in enumerate(nums):

            l=0; r=len(nums)-1

            while l<r:
                if i == l:
                    l+=1
                    continue
                elif i == r:
                    r-=1
                    continue

                s = num + nums[l] + nums[r]
                if s == 0:
                    ans.add(tuple(sorted([num, nums[l], nums[r]])))
                    l+=1
                    r-=1
                elif s < 0:
                    l+=1
                else:
                    r-=1

        return list(ans)