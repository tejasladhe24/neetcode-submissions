class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A,B = nums1,nums2
        if len(A)>len(B):
            A,B = B,A

        total = len(A)+len(B)
        half = total//2

        l,r = 0,len(A)-1

        while True:
            i = (l+r)//2
            j = (half-1) -i-1

            Aleft = A[i] if i>=0 else float("-inf")
            Aright = A[i+1] if i+1<len(A) else float("inf")
            Bleft = B[j] if j>=0 else float("-inf")
            Bright = B[j+1] if j+1<len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft,Bleft) + min(Aright,Bright)) / 2.0 
                else:
                    return min(Aright,Bright)
            
            elif Bleft > Aright:
                l = i+1
            else:
                r = i-1