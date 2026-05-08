class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)-1

        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break
            elif matrix[mid][0] < target:
                l = mid+1
            else:
                r = mid-1

        res = matrix[mid]

        l,r=0,len(res)-1
        while l<=r:
            mid = (l+r)//2
            val = res[mid]
            if val == target:
                return True
            elif val < target:
                l = mid+1
            else:
                r = mid-1

        return False