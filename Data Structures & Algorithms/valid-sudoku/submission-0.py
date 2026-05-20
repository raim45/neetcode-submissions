class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # # rows
        # for i in range(len(board)):
        #     before = []
        #     for j in range(len(board)):
        #         if board[i][j] != ".":
        #             before.append(i)
        #     after = set(before)
        #     if len(after) != len(before):
        #         return False


        # # columns
        # for i in range(len(board)):
        #     before = []
        #     for j, val in enumerate(len(board)):
        #         if board[j][i] != ".":
        #             continue
        #         else:
        #             before.append(val)
        #     after = set(before)
        #     if len(after) != len(before):
        #         return False
        # #3 by 3 block
        # return True
        # for i in range(len(board)):
        #     before = []
        #     for j, val in enumerate():
        #         if board[j][i] != ".":
        #             continue
        #         else:
        #             before.append(val)
        #     after = set(before)
        #     if len(after) != len(before):
        #         return False
        rows = defaultdict(set)
        squares = defaultdict(set)
        cols = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in squares[r // 3, c // 3]) or (board[r][c] in rows[r]) or (board[r][c] in cols[c]) :
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r // 3, c // 3].add(board[r][c])
        return True




        


        