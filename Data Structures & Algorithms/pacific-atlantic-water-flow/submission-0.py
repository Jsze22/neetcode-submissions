class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        where = []

        def helper(x, y, curr_x, curr_y, prev_height):

            # bounds FIRST
            if (
                curr_x < 0 or
                curr_y < 0 or
                curr_x >= len(heights) or
                curr_y >= len(heights[0])
            ):
                return

            if (curr_x, curr_y) in visited:
                return

            # water can't flow uphill
            if heights[curr_x][curr_y] > prev_height:
                return

            visited.add((curr_x, curr_y))

            # Pacific
            if curr_x == 0 or curr_y == 0:
                both[0] = True

            # Atlantic
            if (
                curr_x == len(heights) - 1 or
                curr_y == len(heights[0]) - 1
            ):
                both[1] = True

            helper(x, y, curr_x + 1, curr_y, heights[curr_x][curr_y])
            helper(x, y, curr_x - 1, curr_y, heights[curr_x][curr_y])
            helper(x, y, curr_x, curr_y + 1, heights[curr_x][curr_y])
            helper(x, y, curr_x, curr_y - 1, heights[curr_x][curr_y])

        for x in range(len(heights)):
            for y in range(len(heights[x])):

                both = [False, False]
                visited = set()

                helper(x, y, x, y, heights[x][y])

                if both[0] and both[1]:
                    where.append([x, y])

        return where