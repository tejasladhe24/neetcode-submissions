class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _t,_i = stack.pop()
                res[_i] = i - _i

            stack.append((temp,i))

        return res