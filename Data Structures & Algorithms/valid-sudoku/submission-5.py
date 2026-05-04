from typing import List
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

class Solution:
    def _are_all_unique(self, nums):
        return len(set(nums)) == len(nums)
    
    def _clean_list(self, items):
        return [item for item in items if item != "."]

    def _flatten_lists(self, lists):
        return sum(lists, [])

    def _validate_row(self, board, i):
        items = self._clean_list(board[i])
        return self._are_all_unique(items)

    def _validate_col(self, board, j):
        items = self._clean_list([board[pos][j] for pos in range(9)])
        return self._are_all_unique(items)

    def _validate_block(self, board, i, j):
        items = [arr[j*3:(j+1)*3] for arr in board[i*3:(i+1)*3]]
        items = self._flatten_lists(items)
        items = self._clean_list(items)
        return self._are_all_unique(items)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        stop_event = threading.Event()

        def task_validate_blocks():
            for i in range(3):
                for j in range(3):
                    if stop_event.is_set():
                        return None
                    if not self._validate_block(board, i, j):
                        return False
            return True

        def task_validate_rows():
            for i in range(9):
                if stop_event.is_set():
                    return None
                if not self._validate_row(board, i):
                    return False
            return True

        def task_validate_cols():
            for j in range(9):
                if stop_event.is_set():
                    return None
                if not self._validate_col(board, j):
                    return False
            return True

        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = [
                executor.submit(task_validate_blocks),
                executor.submit(task_validate_rows),
                executor.submit(task_validate_cols),
            ]

            for future in as_completed(futures):
                result = future.result()

                if result is False:
                    stop_event.set()

                    for f in futures:
                        f.cancel()

                    return False

            return True