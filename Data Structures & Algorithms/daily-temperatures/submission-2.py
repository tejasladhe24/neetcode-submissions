class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i,elem in enumerate(temperatures):
            stack = [elem]
            j=i+1
            while j<len(temperatures):
                if temperatures[j] <= stack[0]:
                    stack.append(temperatures[j])
                    j+=1
                    if j == len(temperatures):
                        res.append(0)
                        break
                else:
                    res.append(len(stack))
                    break
        
        res.append(0)

        return res