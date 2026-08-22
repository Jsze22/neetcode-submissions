class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        truth = False
        visited = set()

        def helper(curr, x, y):
            nonlocal truth

            length = len(curr)

            if curr != word[:length]:
                return

            if len(curr) == len(word):
                truth = True
                return

            visited.add((x, y))

            if x + 1 < len(board) and (x + 1, y) not in visited:
                helper(curr + board[x + 1][y], x + 1, y)

            if y + 1 < len(board[0]) and (x, y + 1) not in visited:
                helper(curr + board[x][y + 1], x, y + 1)

            if x - 1 >= 0 and (x - 1, y) not in visited:
                helper(curr + board[x - 1][y], x - 1, y)

            if y - 1 >= 0 and (x, y - 1) not in visited:
                helper(curr + board[x][y - 1], x, y - 1)

            visited.remove((x, y))

        for x in range(len(board)):
            for y in range(len(board[0])):
                helper(board[x][y], x, y)

        return truth