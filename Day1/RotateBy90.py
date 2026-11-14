"""
================================================================================
DSA STUDY JOURNAL — LEETCODE 48: ROTATE IMAGE (MEDIUM)
================================================================================

1. PROBLEM STATEMENT & GOAL:
   - Given an `n x n` 2D matrix representing an image, rotate the image by 
     90 DEGREES CLOCKWISE.
   - Crucial Rule: Modify the matrix IN-PLACE (`O(1)` extra space). Do NOT 
     allocate a second 2D matrix.
   - LeetCode's function signature returns `None` (it checks `matrix` directly 
     after your function finishes).

2. CORE INTUITION (THE 2-STEP MATRIX MAGIC: TRANSPOSE + REVERSE):
   Rotating any square matrix 90 degrees clockwise breaks down into two simple 
   in-place operations:

   - [Step 1] Transpose the Matrix (Flip diagonally across top-left to bottom-right):
       Rows become columns, and columns become rows (`matrix[i][j]` <-> `matrix[j][i]`).
       Before:             After Transpose:
       [1, 2, 3]           [1, 4, 7]
       [4, 5, 6]    --->   [2, 5, 8]
       [7, 8, 9]           [3, 6, 9]

   - [Step 2] Reverse Every Row (Flip horizontally left-to-right):
       Reversing each row puts the columns into their final 90-degree clockwise 
       positions!
       After Transpose:    After Reverse Rows (90° Clockwise):
       [1, 4, 7]           [7, 4, 1]
       [2, 5, 8]    --->   [8, 5, 2]
       [3, 6, 9]           [9, 6, 3]

3. KEY "WHY" NOTES & EDGE CASES (MUST-REMEMBER RULES):
   - Why `for j in range(i + 1, n):` in Transpose (and NOT `range(n)`)?
       * If `j` started at `0` (`range(n)`), you would swap `(i, j)` with `(j, i)` 
         in the upper triangle, and then SWAP THEM BACK when visiting the lower 
         triangle—leaving the matrix completely unchanged!
       * Starting `j` at `i + 1` visits ONLY the upper-right triangle above the 
         main diagonal, ensuring every pair swaps ONCE (and skips the diagonal 
         `i == j`, which doesn't move anyway).
   - Bonus Trick (90° Counter-Clockwise Rotation):
       * Reverse each row FIRST, then Transpose (or Transpose first, then 
         reverse the columns).
   - LeetCode Submission vs. Local Printing:
       * Returning `matrix` at the end is super convenient for local testing 
         (`print(ans)`), and LeetCode's Python judge ignores return values on 
         `-> None` problems—though removing `return matrix` matches the strict 
         signature cleanly.

4. COMPLEXITY ANALYSIS:
   - Time Complexity : O(n^2) -> Every cell in the `n x n` grid is visited once 
                                 during transpose and once during row reversal.
   - Space Complexity: O(1)   -> Purely in-place swaps; zero extra grids used.
================================================================================
"""

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        # Step 1: Transpose in-place (swap upper triangle across main diagonal)
        # Standard Formula for 2D Transpose -> j starts at i + 1
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row in-place to complete the 90° clockwise rotation
        for row in matrix:
            row.reverse()

        # Optional for local testing (LeetCode checks `matrix` in-place directly)
        return matrix


# ==============================================================================
# LOCAL TEST CASES FOR REFERENCE
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()

    # Case 1: 3x3 Matrix
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Case 1 (3x3) ->", sol.rotate(matrix1))
    # Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    # Case 2: 4x4 Matrix
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print("Case 2 (4x4) ->", sol.rotate(matrix2))
    # Expected: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
