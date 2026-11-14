nums = [-1, 0, 1, 2, -1, -4]

def threesum(nums:list[int]):
    nums.sort()
    res = []

    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l = i + 1
        r = len(nums)-1

        while l < r:
            total = nums[i] + nums[l] + nums[r]

            if total == 0:
                res.append([nums[i] , nums[l] , nums[r]])

                while l < r and nums[l+1] == nums[l]:
                    l += 1
                while l < r and nums[r-1] == nums[r]:
                    r -= 1
 
                l += 1
                r -= 1

            elif total < 0:
                l += 1
            elif total > 0:
                r -= 1
    return res
print(threesum(nums))


# =====================================================
# DSA NOTES: 3Sum (LeetCode 15)
# =====================================================

# DATA STRUCTURE:
# Array

# ALGORITHM:
# Sorting + Two Pointers

# TECHNIQUE:
# Fixed Element + Two Pointer Traversal

# APPROACH:
# 1. Sort the array in ascending order.
# 2. Iterate through the array using an outer loop.
# 3. Fix the current element as the first element.
# 4. Skip duplicate fixed elements to avoid repeated triplets.
# 5. Break if the fixed element is greater than zero.
# 6. Initialize left pointer at i + 1.
# 7. Initialize right pointer at the last index.
# 8. Calculate the sum of the three elements.
# 9. If sum equals zero, store the triplet.
# 10. Skip duplicate values using both pointers.
# 11. Move both pointers inward after finding a triplet.
# 12. If sum is less than zero, move left forward.
# 13. If sum is greater than zero, move right backward.
# 14. Return all unique triplets.

# IMPORTANT LOGIC:
# Sorting allows efficient Two Pointer traversal.
# Fix one element and search for the remaining two.
# Moving left increases the sum.
# Moving right decreases the sum.
# Duplicate handling ensures unique triplets.
# Early termination is possible when nums[i] > 0.

# TIME COMPLEXITY:
# O(n²) - Sorting takes O(n log n).
# The outer loop takes O(n).
# Each Two Pointer traversal takes O(n).

# AUXILIARY SPACE COMPLEXITY:
# O(1) - Excluding sorting implementation and output storage.

# KEY LEARNINGS:
# - Sorting
# - Two Pointers
# - Fixed Element Technique
# - Duplicate Handling
# - Early Termination
# - Pointer Movement
# - Time Complexity Optimization

# INTERVIEW EXPLANATION:
# I used Sorting combined with the Two Pointers technique.
# First, I sort the array to make pointer movement predictable.
# I fix one element using an outer loop.
# Then, I search for the remaining pair using left and right pointers.
# Based on the calculated sum, I adjust the pointers.
# I handle duplicates to ensure unique triplets.
# Finally, I return all valid triplets.