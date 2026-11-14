"""
================================================================================
LEETCODE 26: REMOVE DUPLICATES FROM SORTED ARRAY (PYTHON 3)
================================================================================

1. PROBLEM GOAL:
   - Given a sorted integer list `nums`, remove duplicates IN-PLACE so each 
     unique element appears only once.
   - Maintain the original sorted relative order.
   - Return `k`, the total count of unique elements.
   - LeetCode's judge checks ONLY the first `k` elements (`nums[:k]`) and 
     ignores any leftover elements from index `k` to the end.

2. PATTERN: READ / WRITE TWO POINTERS (IN-PLACE OVERWRITING)
   - Fast Pointer (`j`): Scans through the entire array from index 1 to l - 1,
     looking for brand-new unique numbers.
   - Slow Pointer (`k`): Does 3 critical jobs at once:
       [Job 1] Open Slot Bookmark : Points to the next empty index where a new
                                    unique number should be placed.
       [Job 2] Condition Reference: `nums[k - 1]` looks 1 step behind `k` to 
                                    check the LAST saved unique number.
       [Job 3] In-Place Writer    : `nums[k] = nums[j]` overwrites duplicate 
                                    spots at the front of the list.
       [Bonus] Final Count        : Once the loop ends, `k` equals the exact 
                                    number of unique elements found.

3. WHY WE INITIALIZE `k = 1` AND START `j` AT `1`:
   - `nums[0]` is ALREADY in the right spot at the front of the list and has no 
     element before it to duplicate.
   - Leaving index 0 untouched guarantees at least 1 unique element exists 
     (as long as `nums` is not empty) and reserves index 1 as the first open slot.

4. COMPLEXITY ANALYSIS:
   - Time Complexity : O(n) -> Both pointers traverse the list at most once.
   - Space Complexity: O(1) -> Modifies `nums` in-place; zero extra arrays used.

5. LEVEL-UP TIP (LEETCODE 80):
   - If a problem allows up to 2 duplicates instead of 1, simply change:
     `k = 2`, `range(2, l)`, and `if nums[j] != nums[k - 2]:`.
================================================================================
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # EDGE CASE: If the list is completely empty, there are 0 unique elements.
        if not nums:
            return 0

        # Initialize `k` at 1 because index 0 is already unique and locked in.
        k = 1
        l = len(nums)

        # Fast pointer `j` scans every element starting from index 1.
        for j in range(1, l):
            # Compare incoming element `nums[j]` against the LAST saved unique 
            # element `nums[k - 1]` (NEVER compare against `nums[k]`, which holds 
            # uncleaned/leftover data).
            if nums[j] != nums[k - 1]:
                # Place the new unique number into the open slot at `k`.
                nums[k] = nums[j]
                # Advance `k` to point to the next available open slot.
                k += 1

        # Return the count of unique elements (LeetCode slices `nums[:k]` to verify).
        return k


# ==============================================================================
# LOCAL TESTING & PRINTING THE CLEAN LIST YOURSELF
# ==============================================================================
if __name__ == "__main__":
    nums = [0, 0, 1, 1, 2, 4, 4, 6, 7, 7, 9]
    sol = Solution()
    
    # Run the LeetCode function to get `k` and modify `nums` in-place
    k = sol.removeDuplicates(nums)

    print("Unique count (k):", k)                 # Output: 7
    print("Raw array after loop:", nums)          # Output: [0, 1, 2, 4, 6, 7, 9, 6, 7, 7, 9]
    
    # Option A: View the unique elements using slicing (non-destructive)
    print("Clean slice (nums[:k]):", nums[:k])    # Output: [0, 1, 2, 4, 6, 7, 9]

    # Option B: Permanently delete leftover junk from the end of `nums`
    del nums[k:]
    print("Trimmed list in-place:", nums)         # Output: [0, 1, 2, 4, 6, 7, 9]
