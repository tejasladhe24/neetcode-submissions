class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data = {}

        for elem in nums:
            data[elem] = True

        curr = []; longest=0

        for num in nums:
            curr = [num]
            val = num

            while True:
                val = val+1
                if val in data:
                    curr.append(val)
                else:
                    break
            
            longest = max(longest,len(curr))
        
        return longest

