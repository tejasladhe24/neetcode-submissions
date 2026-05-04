class Solution:
    def _are_all_unique(self,nums):
        return len(list(set(nums))) == len(nums)
    
    def _clean_list(self, items):
        return [item for item in items if item!="."]

    def _flatten_lists(self, lists):
        return sum(lists,[])

    def _validate_row(self,board,i):
        """
        Validates ith row in board; i ∈ range(9)
        """
        items = self._clean_list(board[i])
        return self._are_all_unique(items)

    def _validate_col(self,board,j):
        """
        Validates jth column in board; j ∈ range(9)
        """
        items = self._clean_list([board[pos][j] for pos in range(9)])
        return self._are_all_unique(items)

    def _validate_block(self,board,i,j):
        """
        Validates B(i,j) 3x3 block where i,j ∈ [0,1,2],
        """
        items = [arr[j*3:(j+1)*3] for arr in board[i*3:(i+1)*3]]
        items = self._flatten_lists(items)
        items = self._clean_list(items)
        return self._are_all_unique(items)

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def task_validate_blocks():
            # 9 blocks
            # captures 3x3 squares into 1d flat array
            for i in range(3):
                for j in range(3):
                    if not self._validate_block(board,i,j):
                        return False
            return True

        def task_validate_rows():
            # 9 rows
            for i in range(9):
                if not self._validate_row(board,i):
                    return False
            return True

        def task_validate_cols():
            # 9 cols
            for j in range(9):
                if not self._validate_col(board,j):
                    return False
            return True
        
        return task_validate_blocks() and task_validate_rows() and task_validate_cols()