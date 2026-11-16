class Solution:
    def subsubarray(self ,nums: list[int], k: int ) -> int:

        if not nums:
            return -1

        left = 0
        curr_sum = 0
        max_sum = 0

        count = {}

        for right in range(len(nums)):
            val = nums[right]
            curr_sum += nums[right]
            count[val] = count.get(val , 0) + 1

            while len(count) > k:
                l_val = nums[left]
                curr_sum -= l_val
                count[l_val] -= 1
                
                if count[l_val] == 0:
                    del count[l_val]

                left += 1 

            max_sum = max(curr_sum ,max_sum)

        return max_sum

nums = [1,2,1,2,4]      
k = 2
sol = Solution()
ans = sol.subsubarray(nums ,k)
print(ans)




"""
================================================================================
DSA STUDY JOURNAL — MAXIMUM SUM SUBARRAY WITH AT MOST K DISTINCT ELEMENTS
================================================================================

1. PROBLEM STATEMENT & GOAL:
   - Given an array of non-negative integers `nums` and an integer `k`, find the 
     MAXIMUM SUM of any contiguous subarray containing AT MOST `k` distinct 
     (unique) elements.
   - Edge Case: If `k == 0` or `nums` is empty, return `0`.

2. CORE INTUITION (VARIABLE SLIDING WINDOW + FREQUENCY DICT):
   - Unlike LeetCode 3 (where 0 duplicates were allowed, so `set()` worked), 
     duplicates ARE allowed here!
   - Use a dictionary `counts` mapping `{element: frequency_in_window}`:
       * `len(counts)` = exact number of distinct elements in `[left ... right]`.
       * When shrinking from `left`, decrement `counts[nums[left]]`, and ONLY 
         delete the key (`del counts[nums[left]]`) when its frequency hits `0`.

3. COMPLEXITY ANALYSIS:
   - Time Complexity : O(n) -> Both `right` and `left` move forward at most `n` times.
   - Space Complexity: O(k) -> Dictionary holds at most `k + 1` keys at any moment.
================================================================================
"""

class Solution:
    def maxSumAtMostKDistinct(self, nums: list[int], k: int) -> int:
        if k == 0 or not nums:
            return 0

        counts = {}      # Tracks {num: frequency} inside current window
        left = 0         # Left boundary of sliding window
        curr_sum = 0     # Sum of elements inside [left ... right]
        max_sum = 0      # Best valid subarray sum found so far

        for right in range(len(nums)):
            # 1. Expand window to include nums[right]
            val = nums[right]
            curr_sum += val
            counts[val] = counts.get(val, 0) + 1

            # 2. Shrink from left while distinct elements exceed k
            while len(counts) > k:
                left_val = nums[left]
                curr_sum -= left_val
                counts[left_val] -= 1
                
                # Only remove the key when zero copies remain in the window
                if counts[left_val] == 0:
                    del counts[left_val]
                left += 1

            # 3. Record max sum for this valid window
            max_sum = max(max_sum, curr_sum)

        return max_sum


# ==============================================================================
# LOCAL TEST CASES FOR REFERENCE
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()

    # Case 1: Subarray [1, 2, 1, 2] has 2 distinct elements and sum = 6
    print("Case 1 ->", sol.maxSumAtMostKDistinct([1, 2, 1, 2, 3], 2))  # Expected: 6

    # Case 2: k = 1 (longest/max-sum streak of identical numbers -> [4, 4, 4] = 12)
    print("Case 2 ->", sol.maxSumAtMostKDistinct([4, 4, 4, 1, 9], 1))  # Expected: 12

    # Case 3: k >= total distinct elements (entire array is valid -> sum = 15)
    print("Case 3 ->", sol.maxSumAtMostKDistinct([1, 2, 3, 4, 5], 5))  # Expected: 15
