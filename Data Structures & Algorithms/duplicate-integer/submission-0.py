class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data = {}

        for num in nums:
            if num in data:
                return True
            data[num] = True

        return False