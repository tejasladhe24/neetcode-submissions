class Solution:
    def areAllUnique(self,nums):
        return len(list(set(nums))) == len(nums)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9 blocks
        for i in range(3):
            for j in range(3):
                items = sum([arr[j*3:(j+1)*3] for arr in board[i*3:(i+1)*3]],[])
                items = [item for item in items if item != "."]
                if not self.areAllUnique(items):
                    return False

        # 9 rows
        for i in range(9):
            items = [item for item in board[i] if item != "."]
            if not self.areAllUnique(items):
                return False

        # 9 cols
        for i in range(9):
            items = [board[j][i] for j in range(9) if board[j][i] != "."]
            if not self.areAllUnique(items):
                return False

        return True