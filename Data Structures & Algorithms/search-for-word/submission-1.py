class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        truth = False
        visited = set()

        def helper(curr, x, y):
            nonlocal truth
            xbound = len(board)
            ybound = len(board[x])
            length = len(curr)
            if curr != word[:length]:
                return
            
            if len(curr) == len(word):
                truth = True
            else:
                if x+1 < xbound and (x+1, y) not in visited:
                    visited.add((x+1, y))
                    helper(curr + board[x+1][y], x+1, y)
                    visited.remove((x+1, y))
                if y+1 < ybound and (x,y+1) not in visited:
                    visited.add((x,y+1))
                    helper(curr+ board[x][y+1], x, y+1)
                    visited.remove((x,y+1))
                if x-1 >= 0 and (x-1,y) not in visited:
                    visited.add((x-1,y))
                    helper(curr+board[x-1][y], x-1, y)
                    visited.remove((x-1,y))
                if y - 1 >=0 and (x,y-1) not in visited:
                    visited.add((x,y-1))
                    helper(curr+board[x][y-1], x, y-1)
                    visited.remove((x,y-1))


        for x in range(len(board)):
            for y in range(len(board[x])):
                 visited.add((x, y))
                 helper(board[x][y], x, y)
                 visited.remove((x, y))


        return truth



        

        