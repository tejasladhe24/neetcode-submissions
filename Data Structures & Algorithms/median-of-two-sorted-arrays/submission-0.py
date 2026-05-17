class Solution:
    def binary_insert(self, nums, value):
            l,r = 0, len(nums)
            while l < r:
                mid = (l+r)//2
                if nums[mid] < value:
                    l = mid + 1
                else:
                    r = mid
            nums.insert(l, value)

    def binarySort(self, nums: List[int]) -> List[int]:
        _nums = []
        for num in nums:
            self.binary_insert(_nums, num)
        return _nums

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = self.binarySort(nums1+nums2)
        n = len(nums)
        mid = n//2

        if n%2 == 0:
            return sum(nums[mid-1:mid+1])/2
        else:
            return nums[mid]
