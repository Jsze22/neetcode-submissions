class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter =0

        

        def helper(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]) or grid[x][y] == "0":
                return

            grid[x][y] = "0"

            helper(x-1, y)
            helper(x+1, y)
            helper(x, y+1)
            helper(x, y-1)
        
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1":
                    counter +=1
                    helper(x, y)
                    
        return counter
