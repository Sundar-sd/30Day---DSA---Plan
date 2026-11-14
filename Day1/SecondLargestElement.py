"""
================================================================================
DSA STUDY JOURNAL — SECOND LARGEST ELEMENT IN ARRAY (EASY)
================================================================================

1. PROBLEM STATEMENT & GOAL:
   - Given an array of integers `nums`, find and return the SECOND LARGEST 
     DISTINCT element in a single pass without sorting.
   - If no second largest distinct element exists (e.g., all elements are 
     identical like, or the list has fewer than 2 elements), 
     return `-1`.

2. CORE INTUITION ("GOLD & SILVER MEDAL" TRACKING):
   - Track two variables as you scan the array once from left to right:
       * `first`  -> Gold Medalist (largest number seen so far).
       * `second` -> Silver Medalist (second largest distinct number seen so far).

   - For every `num` in `nums`, check two conditions:
       [Case 1: `if num > first:`]
           Someone beat the #1 record! Demote the old Gold medalist to Silver 
           (`second = first`), then update `first = num`.
       [Case 2: `elif num > second and num < first:`]
           Someone didn't beat 1st place (and isn't tied with 1st place), BUT 
           did beat 2nd place! Update `second = num`.
       [Case 3: Everything else (`num == first` or `num <= second`)]
           Ignore completely.

3. KEY "WHY" NOTES & EDGE CASES (FROM MY DEBUGGING):
   - Why initialize both with `float("-inf")` instead of `0` or `-1`?
       * Ensures negative arrays like `[-1, -5, -3]` work properly! Every real 
         negative number is strictly greater than `-inf`.
       * Also doubles as a clean "not found" flag at the end: if `second` is 
         still `float("-inf")`, we know no second largest element existed.
   - Why `num < first` inside the `elif` condition?
       * Blocks duplicate maximums! In `[10, 10, 5]`, the second `10` fails 
         `10 < 10`, preventing `10` from taking both 1st and 2nd place.
   - Local Testing vs. Platform Submission:
       * Returning `(first, second)` is great for local debugging, while coding 
         platforms expect a single integer (`second` or `-1`).

4. COMPLEXITY ANALYSIS:
   - Time Complexity : O(n) -> Single pass through `nums`.
   - Space Complexity: O(1) -> Only two variables (`first` and `second`) used.
================================================================================
"""

class Solution:
    def getSecondLargest(self, nums: list[int]) -> int:
        # Initialize with negative infinity to safely handle negative arrays
        first = float("-inf")
        second = float("-inf")

        for num in nums:
            # Case 1: New largest number found -> demote old `first` to `second`
            if num > first:
                second = first
                first = num

            # Case 2: Strictly smaller than `first` (blocks duplicates), but 
            # greater than current `second`
            elif num > second and num < first:
                second = num

        # Return `second` if found; otherwise return -1
        return second if second != float("-inf") else -1


# ==============================================================================
# LOCAL TEST CASES FOR REFERENCE
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()

    # Case 1: Negative numbers test (my custom test case)
    print("Case 1 [-1, -5, -3] ->", sol.getSecondLargest([-1, -5, -3]))  # Expected: -3

    # Case 2: Duplicate largest element
    print("Case 2 [10, 10, 5]  ->", sol.getSecondLargest([10, 10, 5]))   # Expected: 5

    # Case 3: All elements identical (no second largest exists)
    print("Case 3 [7, 7, 7]    ->", sol.getSecondLargest([7, 7, 7]))     # Expected: -1

