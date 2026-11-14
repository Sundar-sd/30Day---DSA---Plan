"""
================================================================================
DSA STUDY JOURNAL — LEETCODE 88: MERGE SORTED ARRAY (EASY)
================================================================================

1. PROBLEM STATEMENT & GOAL:
   - Given two non-decreasing sorted arrays `nums1` (length `m + n`) and 
     `nums2` (length `n`), merge them into a single sorted array IN-PLACE 
     inside `nums1`.
   - The first `m` elements of `nums1` hold real values; the last `n` elements 
     are `0`s acting as empty buffer slots.
   - Return NOTHING (`None`). Modify `nums1` directly with O(1) extra space.

2. CORE INTUITION (WHY WE MERGE BACKWARDS — RIGHT TO LEFT):
   - Merging from the front (left to right) fails because placing elements 
     from `nums2` into `nums1` overwrites unread elements in `nums1`.
   - Because both arrays are sorted, all the BIGGEST numbers sit at the right 
     ends, and all the EMPTY `0` slots sit at the back of `nums1`.
   - Filling `nums1` from the back (`k = m + n - 1`) with the largest elements 
     first guarantees we only overwrite empty `0` slots and NEVER touch an 
     unread number in `nums1`.

3. THREE-POINTER ROLES:
   - `i = m - 1`     -> Scans real elements of `nums1` from right to left.
   - `j = n - 1`     -> Scans elements of `nums2` from right to left.
   - `k = m + n - 1` -> Write-pointer tracking the next empty slot from the back.

4. KEY "WHY" NOTES & EDGE CASES:
   - Why ONLY `while j >= 0:` for leftovers (and NO `while i >= 0:` loop)?
       * Case A (`i` hits `-1` first): `nums1` held larger numbers that moved to 
         the back, leaving smaller numbers still sitting in `nums2`. We MUST copy 
         those remaining `nums2` elements into the front slots of `nums1`.
       * Case B (`j` hits `-1` first): All of `nums2` is already placed! Any 
         remaining elements in `nums1` are ALREADY sitting inside `nums1` in 
         their exact sorted positions at the front—zero work needed.
   - Empty `nums1` Edge Case (`m = 0`, e.g., `nums1 =`, `nums2 =`):
       `i` starts at `-1`, so the first `while` loop is skipped completely, and 
       `while j >= 0:` copies all of `nums2` straight into `nums1`.

5. COMPLEXITY ANALYSIS:
   - Time Complexity : O(m + n) -> Every element in both arrays is visited once.
   - Space Complexity: O(1)     -> Purely in-place; zero extra lists allocated.
================================================================================
"""

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Initialize three pointers at the right ends
        i = m - 1          # Last real element in nums1
        j = n - 1          # Last element in nums2
        k = m + n - 1      # Last empty buffer slot in nums1

        # Step 1: Compare from the back and place the larger element at index k
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Step 2: Copy any leftover smaller elements from nums2 (if i hit -1 first)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


# ==============================================================================
# LOCAL TEST CASES FOR REFERENCE
# ==============================================================================
