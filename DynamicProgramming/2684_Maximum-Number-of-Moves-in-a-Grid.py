class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        maximum = 0

        memo = [[-1] * col for _ in range(row)]

        def dfs(r, c):
            if memo[r][c] != -1:
                return memo[r][c]
            
            max_moves = 0

            directions = [(-1, 1), (0, 1), (1, 1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] > grid[r][c]:
                    max_moves = max(max_moves, 1 + dfs(nr, nc))
            
            memo[r][c] = max_moves
            return max_moves
        
        for i in range(row):
            maximum = max(maximum, dfs(i, 0))
        
        return maximum

            
