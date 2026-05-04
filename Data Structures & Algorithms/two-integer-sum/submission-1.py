class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = dict()

        for i,elem in enumerate(nums):
            if target-elem in data:
                return [data[target-elem],i]
            else:
                data[elem]=i

        return [-1,-1]
