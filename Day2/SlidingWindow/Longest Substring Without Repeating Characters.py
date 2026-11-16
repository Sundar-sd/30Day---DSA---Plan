class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        max_len = 0
        seen = set()

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            max_len = max(max_len , right - left  + 1)

        return max_len

s = ('abcacdliahifowegfi9pfowgf')
sol = Solution()
ans = sol.lengthOfLongestSubstring(s)
print(ans)


"""
================================================================================
DSA STUDY JOURNAL — LEETCODE 3: LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
================================================================================

1. PROBLEM STATEMENT & GOAL:
   - Given a string `s`, find the length of the LONGEST CONTIGUOUS SUBSTRING 
     that contains NO duplicate characters.
   - Substring vs. Subsequence: A substring must be continuous with zero gaps 
     (e.g., in "pwwkew", "wke" is a valid substring of length 3, while "pwke" 
     is a subsequence and NOT valid).

2. CORE INTUITION (VARIABLE-SIZE SLIDING WINDOW + HASH SET):
   - Maintain a dynamic window `[left ... right]` representing the current 
     duplicate-free substring, backed by a Python `set()` (`seen`) for O(1) 
     membership checks.
   - As `right` expands forward one character at a time:
       [Step 1] Shrink (`while s[right] in seen:`):
           If the incoming character `s[right]` is already inside our window, 
           repeatedly remove `s[left]` from `seen` and move `left += 1` until 
           the old duplicate is evicted.
       [Step 2] Expand (`seen.add(s[right])`):
           Add the new unique character into the window set.
       [Step 3] Record (`right - left + 1`):
           Calculate the current valid window size and update `max_len`.

3. KEY "WHY" NOTES & EDGE CASES:
   - Why `while s[right] in seen:` instead of `if`?
       * The duplicate character might not be at index `left`! For example, in 
         `"pw"` when a second `'w'` arrives, we must remove BOTH `'p'` and the 
         first `'w'` before the window becomes valid again.
   - Why `right - left + 1`?
       * Indices are 0-based and inclusive on both ends. If `left = 2` and 
         `right = 4`, the window covers indices `2, 3, 4` -> `4 - 2 + 1 = 3` chars.
   - Empty String Edge Case (`s = ""`):
       * The `for` loop runs 0 times and cleanly returns `max_len = 0`.

4. COMPLEXITY ANALYSIS:
   - Time Complexity : O(n) -> Both `right` and `left` move forward at most `n` 
                               times across the entire execution (2n = O(n)).
   - Space Complexity: O(min(n, k)) -> Where `k` is the character set size 
                                       (at most 128/256 ASCII chars -> O(1)).
================================================================================
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()       # Tracks characters currently inside [left ... right]
        left = 0           # Left boundary of the sliding window
        max_len = 0        # Longest valid substring length found so far

        # Right pointer expands the window one character at a time
        for right in range(len(s)):
            # Step 1: If duplicate found, shrink window from left until removed
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Step 2: Add the current character into the valid window
            seen.add(s[right])

            # Step 3: Update maximum window length
            max_len = max(max_len, right - left + 1)

        return max_len


# ==============================================================================
# LOCAL TEST CASES FOR REFERENCE
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()

    print("Case 1 'abcabcbb' ->", sol.lengthOfLongestSubstring("abcabcbb"))  # Expected: 3
    print("Case 2 'bbbbb'    ->", sol.lengthOfLongestSubstring("bbbbb"))     # Expected: 1
    print("Case 3 'pwwkew'   ->", sol.lengthOfLongestSubstring("pwwkew"))    # Expected: 3
    print("Case 4 ''         ->", sol.lengthOfLongestSubstring(""))          # Expected: 0
