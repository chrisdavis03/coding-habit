'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

def numIslands(grid: list[list[int]]) -> int: 
    if not grid:
        return 0
    count = 0

    m, n = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or r >=m or c < 0 or c>=n or grid[r][c] != '1':
            return
        grid[r][c] = '0' #marks as visited
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(m):
        for c in range(n):
            if grid[r][c] == '1':
                count+=1
                dfs(r,c)

    return count


if __name__ == '__main__':
    grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
        ]
    grid2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
        ]

    print (f'{numIslands(grid=grid)} islands found.')
    print (f'{numIslands(grid=grid2)} islands found.')
    