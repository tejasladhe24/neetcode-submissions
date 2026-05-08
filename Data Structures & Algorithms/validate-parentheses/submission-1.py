class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_tuples = set([tuple(["{","}"]),tuple(["[","]"]),tuple(["(",")"])])

        for elem in s:
            if len(stack) > 0 and tuple([stack[-1], elem]) in valid_tuples:
                stack.pop()
            else:
                stack.append(elem)

        return len(stack) == 0