
#Greedy Approach : Minimum Adjacent Swaps to Separate Evens and Odds


def min_swaps_to_segregate(nums: list[int]) -> int:
    # --- STRATEGY 1: Move all EVENS to the front ---
    even_swap = 0
    target_slot = 0  # The first even number found must go to index 0
    
    # Loop through the array from left to right
    for current_idx, num in enumerate(nums):
        if num % 2 == 0:
            # Distance to move = current position minus its target position at the front
            even_swap += (current_idx - target_slot)
            # The next even number found will occupy the next slot (index 1, then 2, etc.)
            target_slot += 1

    # --- STRATEGY 2: Move all ODDS to the front ---
    odd_swap = 0
    target_slot = 0   # The first odd number found must go to index 0
    
    # Loop through the array from left to right
    for current_idx, num in enumerate(nums):
        if num % 2 != 0:
            # Distance to move = current position minus its target position at the front
            odd_swap += (current_idx - target_slot)
            # The next odd number found will occupy the next slot
            target_slot += 1

    # Return the absolute minimum swaps between both strategies
    return min(even_swap, odd_swap)


# --- Execution Trace with your exact example ---

nums = [6, 1, 4, 3, 2]
# Indices: 0  1  2  3  4

print(f"Original Array: {nums}")
print(min_swaps_to_segregate(nums))





# =====================================================
# DSA NOTES: Minimum Adjacent Swaps to Separate Evens and Odds
# =====================================================

# DATA STRUCTURE:
# Array

# ALGORITHM:
# Greedy Algorithm

# TECHNIQUE:
# Two-Pass Traversal + Index Tracking

# APPROACH:
# 1. Calculate minimum swaps when all evens come first.
# 2. Calculate minimum swaps when all odds come first.
# 3. Use enumerate() to access both index and value.
# 4. Identify even and odd numbers using modulo (% 2).
# 5. Use target_slot to track the next available position.
# 6. Calculate adjacent swap cost using:
#    current_idx - target_slot
# 7. Compare both strategies using min().
# 8. Return the minimum swap count.

# IMPORTANT LOGIC:
# We don't perform actual swaps or modify the array.
# We only calculate the total movement cost.
# Each element moves to its next available target position.

# TIME COMPLEXITY:
# O(n) - Two complete traversals of the array.

# AUXILIARY SPACE COMPLEXITY:
# O(1) - Only a constant number of variables are used.

# KEY LEARNINGS:
# - Greedy decision making
# - Index manipulation
# - enumerate()
# - Modulo operation
# - Adjacent swap cost calculation
# - Minimum cost optimization

# INTERVIEW EXPLANATION:
# I used a Greedy approach with two independent traversals.
# First, I calculate the cost of placing all evens first.
# Then, I calculate the cost of placing all odds first.
# I track target positions and calculate movement costs
# without performing actual swaps.
# Finally, I return the minimum of both costs.