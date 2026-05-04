class Solution:

    def counter(self, nums):
        data = {}
        for num in nums:
            if num not in data:
                data[num] = 0
            data[num] += 1
        
        return data

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = self.counter(nums)
        n = len(nums)
        buckets = [0]*(n+1)

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)

        res = []

        for i in range(len(buckets)-1,0,-1):
            if buckets[i]!=0:
                res.extend(buckets[i])
            if len(res)>=k:
                break
        
        return res


        
