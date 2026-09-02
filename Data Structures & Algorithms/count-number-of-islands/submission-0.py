class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter =0

        

        def helper(x, y):
            if int(grid[x][y]) == 1:
                grid[x][y] = 0
                if x > 0:
                    helper(x-1, y)
                if x < len(grid) -1:
                    helper(x+1, y)
                if y > 0:
                    helper(x, y-1)
                if y < len(grid[x])-1:
                    helper(x, y+1)

        
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if int(grid[x][y]) == 1:
                    print("hello")
                    counter +=1
                    helper(x, y)
                    
        return counter
