class Solution:
    def shiftGrid(self, grid, k):

        rows = len(grid)
        cols = len(grid[0])

        # Repeat the shift k times
        for _ in range(k):

            # Create a new empty grid
            new_grid = [[0] * cols for _ in range(rows)]

            # Visit every element
            for i in range(rows):
                for j in range(cols):

                    # Last element of the grid
                    if i == rows - 1 and j == cols - 1:
                        new_grid[0][0] = grid[i][j]

                    # Last column of a row
                    elif j == cols - 1:
                        new_grid[i + 1][0] = grid[i][j]

                    # Normal element
                    else:
                        new_grid[i][j + 1] = grid[i][j]

            # Update the grid
            grid = new_grid

        return grid


# ---------------- Main Program ----------------

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

k = 1

obj = Solution()
result = obj.shiftGrid(grid, k)

print("Shifted Grid:")
for row in result:
    print(row)