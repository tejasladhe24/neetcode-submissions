class Solution:
    def _are_all_unique(self,nums):
        return len(list(set(nums))) == len(nums)
    
    def _clean_list(self, items):
        return [item for item in items if item!="."]

    def _flatten_lists(self, lists):
        return sum(lists,[])

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9 blocks
        for i in range(3):
            for j in range(3):
                # capturing 3x3 squares into 1d flat array
                items = [arr[j*3:(j+1)*3] for arr in board[i*3:(i+1)*3]]
                items = self._flatten_lists(items)
                items = self._clean_list(items)
                if not self._are_all_unique(items):
                    return False

        # 9 rows
        for i in range(9):
            items = self._clean_list(board[i])
            if not self._are_all_unique(items):
                return False

        # 9 cols
        for i in range(9):
            items = self._clean_list([board[j][i] for j in range(9)])
            if not self._are_all_unique(items):
                return False

        return True