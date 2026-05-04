class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data = {}

        for elem in nums:
            data[elem] = True

        curr_length = []; longest_length=0

        for num in nums:
            if num-1 in data:
                continue

            curr_length = 1
            next_num = num+1

            while next_num in data:
                curr_length += 1
                next_num += 1
            
            longest_length = max(longest_length,curr_length)
        
        return longest_length

