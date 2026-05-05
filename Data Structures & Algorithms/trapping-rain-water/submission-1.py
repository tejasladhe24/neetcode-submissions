class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0]*n
        max_right = [0]*n

        for i in range(n):
            j = -i-1
            max_left[i] = max(max_left[i-1], height[i])
            max_right[j] = max(max_right[j+1], height[j])

        # print(max_left, max_right)

        total = 0

        for i in range(n):
            pot = min(max_left[i], max_right[i])
            total += max(0, pot - height[i])

        return total