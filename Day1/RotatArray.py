"""
================================================================================
DSA STUDY JOURNAL — LEETCODE 189: ROTATE ARRAY (MEDIUM)
================================================================================

1. PROBLEM STATEMENT & GOAL:
   - Given an integer array `nums`, rotate the array to the RIGHT by `k` steps, 
     where `k` is non-negative.
   - Crucial Rule: Modify `nums` IN-PLACE (`O(1)` extra space) and return 
     NOTHING (`None`).

2. CORE INTUITION (THE 3-STEP REVERSAL TRICK):
   Rotating an array to the right by `k` steps moves the last `k` elements to 
   the front. Instead of shifting elements one by one (which takes slow O(n * k) 
   time), we use three reversals:

   Example: `nums = [1, 2, 3, 4, 5, 6, 7]`, `k = 3`
   - [Step 1] Reverse the ENTIRE array (`nums.reverse()`):
       `[1, 2, 3, 4, 5, 6, 7]`  --->  `[7, 6, 5, 4, 3, 2, 1]`
       *(Notice the last 3 elements `[5, 6, 7]` are now at the front, just backwards!)*

   - [Step 2] Reverse the FIRST `k` elements (`nums[:k]`):
       `[7, 6, 5 | 4, 3, 2, 1]` --->  `[5, 6, 7 | 4, 3, 2, 1]`

   - [Step 3] Reverse the REMAINING `n - k` elements (`nums[k:]`):
       `[5, 6, 7 | 4, 3, 2, 1]` --->  `[5, 6, 7 | 1, 2, 3, 4]`  (Done!)

3. KEY "WHY" NOTES & EDGE CASES (MUST-REMEMBER RULES):
   - Why `k = k % n`?
       * Rotating an array of length `n` by `n` full steps brings it right back 
         to where it started!
       * If `n = 5` and `k = 7`, `7 % 5 = 2` (rotating 7 times is identical to 
         rotating 2 times). Without `% n`, `nums[:k]` would slice past the end 
         of the list and fail when `k > n`.
   - Bonus Tip (Left Rotation by `k` steps):
       * To rotate LEFT instead of right, simply reverse `nums[:k]` and `nums[k:]` 
         FIRST, then reverse the entire list `nums.reverse()` at the end!
   - Interview Pro-Tip (True O(1) Space vs. Python Slicing):
       * `nums[:k]` creates a temporary slice copy in memory (`O(n)` space under 
         the hood). In strict interviews, you can write a tiny two-pointer helper 
         `rev(l, r)` to swap elements in-place for strict `O(1)` memory.

4. COMPLEXITY ANALYSIS:
   - Time Complexity : O(n) -> Every element is reversed twice across the 3 steps.
   - Space Complexity: O(1) auxiliary logic (or O(n) temporary slice memory in Python).
================================================================================
"""

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)

        # Normalize `k` in case `k >= n` (full rotations cancel out)
        k = k % n

        # Step 1: Reverse the entire array in-place
        nums.reverse()

        # Step 2: Reverse the first `k` elements back into forward order
        nums[:k] = reversed(nums[:k])

        # Step 3: Reverse the remaining `n - k` elements back into forward order
        nums[k:] = reversed(nums[k:])


# ==============================================================================
# LOCAL TEST CASES FOR REFERENCE
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()

    # Case 1: Standard right rotation
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(nums1, 3)
    print("Case 1 (k = 3)  ->", nums1)  # Expected: [5, 6, 7, 1, 2, 3, 4]

    # Case 2: Edge case where k > len(nums) (k = 5 on length 2 -> 5 % 2 = 1)
    nums2 = [-1, -100]
    sol.rotate(nums2, 5)
    print("Case 2 (k = 5)  ->", nums2)  # Expected: [-100, -1]

    # Case 3: Edge case where k == len(nums) (k % n == 0 -> unchanged)
    nums3 = [1, 2, 3]
    sol.rotate(nums3, 3)
    print("Case 3 (k = 3)  ->", nums3)  # Expected: [1, 2, 3]

