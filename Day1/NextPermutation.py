"""
================================================================================
DSA STUDY JOURNAL — LEETCODE 31: NEXT PERMUTATION (MEDIUM)
================================================================================

1. PROBLEM STATEMENT & GOAL:
   - Rearrange a list of integers `nums` IN-PLACE into the next lexicographically 
     greater permutation (the closest bigger sequence possible using the exact 
     same numbers, like the next word in a dictionary).
   - Edge Case: If `nums` is already in completely descending order (the max 
     possible arrangement, like [3, 2, 1]), wrap around to the smallest 
     ascending order ([1, 2, 3]).
   - Return NOTHING (`None`). Modify `nums` directly with O(1) extra space.

2. CORE INTUITION (THE 3-STEP TRICK):
   - To make the smallest possible increase, we want to modify digits as far to 
     the RIGHT as possible.
   - Any suffix in descending order (e.g., [5, 4, 2] in) is 
     already maxed out and cannot be rearranged to get bigger.
   
   [Step 1] Find the Pivot (`i`):
       Scan right-to-left starting at `len(nums) - 2` to find the first "dip" 
       where `nums[i] < nums[i + 1]`.
       * If no dip exists (fully descending), `i` walks past index 0 and stops 
         at `-1`.

   [Step 2] Swap with the "Just Barely Bigger" Number (`j`):
       Only runs if `i >= 0` (meaning a valid pivot exists).
       Scan right-to-left from the end (`len(nums) - 1`) to find the first 
       number strictly greater than `nums[i]` (`nums[j] > nums[i]`), then swap 
       `nums[i]` and `nums[j]` ONCE.

   [Step 3] Reverse the Tail (`i + 1` to end):
       Everything after index `i` is guaranteed to be in descending order. 
       Reversing that tail puts it into ascending order (the smallest possible 
       arrangement for those trailing digits).

3. KEY "WHY" NOTES & EDGE CASES (FROM MY DEBUGGING):
   - Why `i >= 0`?
       Protects index 0 (which can be a pivot, e.g., [1, 3, 2]) AND stops `i` 
       at `-1` so Python doesn't wrap around to `nums[-1]` (the last element).
   - Why `>=` instead of `>` (and `<=` instead of `<`)?
       Duplicate numbers next to each other (e.g., [1, 5, 5]) cannot be swapped 
       to make a bigger number. Using `>=` forces `i` to skip duplicates until 
       it finds a strict drop; `<=` forces `j` to find a strictly bigger value.
   - Why `left = i + 1` works automatically for descending arrays:
       If the whole array is descending, `i` ends at `-1`. Step 2 is skipped, 
       and `left = -1 + 1 = 0` reverses the entire array automatically!
   - Indentation Trap:
       `nums[i], nums[j] = nums[j], nums[i]` MUST sit outside (un-indented from) 
       the `while nums[j] <= nums[i]:` loop so the swap executes only once.

4. COMPLEXITY ANALYSIS:
   - Time Complexity : O(n) -> Each pointer traverses the array at most once.
   - Space Complexity: O(1) -> Purely in-place swaps; zero extra lists used.
================================================================================
"""

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        # Step 1: Find the first decreasing element from the right (the Pivot)
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: If a pivot was found, swap it with the smallest number on its 
        # right that is strictly greater than nums[i]
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse everything after index `i` to put the tail in 
        # ascending (smallest) order
        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# ==============================================================================
# LOCAL TEST CASES FOR REFERENCE
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()

    # Case 1: Standard middle pivot
    case1 = [1, 3, 5, 4, 2]
    sol.nextPermutation(case1)
    print("Case 1 [1, 3, 5, 4, 2] ->", case1)  # Expected: [1, 4, 2, 3, 5]

    # Case 2: Fully descending wrap-around (i becomes -1)
    case2 = [3, 2, 1]
    sol.nextPermutation(case2)
    print("Case 2 [3, 2, 1]       ->", case2)  # Expected: [1, 2, 3]

    # Case 3: Duplicate elements check
    case3 = [1, 5, 5]
    sol.nextPermutation(case3)
    print("Case 3 [1, 5, 5]       ->", case3)  # Expected: [5, 1, 5]
