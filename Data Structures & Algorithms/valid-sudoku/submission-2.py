class Solution:
    def areAllUnique(self,nums):
        return len(list(set(nums))) == len(nums)
    
    def cleanList(self, items):
        return [item for item in items if item!="."]

    def flattenLists(self, lists):
        return sum(lists,[])

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9 blocks
        for i in range(3):
            for j in range(3):
                # capturing 3x3 squares into 1d flat array
                items = [arr[j*3:(j+1)*3] for arr in board[i*3:(i+1)*3]]
                items = self.flattenLists(items)
                items = self.cleanList(items)
                if not self.areAllUnique(items):
                    return False

        # 9 rows
        for i in range(9):
            items = self.cleanList(board[i])
            if not self.areAllUnique(items):
                return False

        # 9 cols
        for i in range(9):
            items = self.cleanList([board[j][i] for j in range(9)])
            if not self.areAllUnique(items):
                return False

        return True