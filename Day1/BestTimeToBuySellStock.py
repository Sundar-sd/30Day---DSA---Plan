"""
================================================================================
DSA STUDY JOURNAL — LEETCODE 121: BEST TIME TO BUY AND SELL STOCK (EASY)
================================================================================

1. PROBLEM STATEMENT & GOAL:
   - Given a list `prices` where `prices[i]` is the price of a stock on day `i`, 
     find the MAXIMUM PROFIT you can achieve from ONE buy and ONE sell.
   - Crucial Rule: You MUST buy BEFORE you sell (time only moves forward, so 
     you cannot buy on day 4 and sell on day 1).
   - If no profit is possible (e.g., prices drop every single day like 
     ), return `0`.

2. CORE INTUITION ("TRACK CHEAPEST BUY SO FAR"):
   - Instead of checking every pair of days (which takes slow O(n^2) nested 
     loops), scan the prices ONCE from left to right while remembering:
       * `min_price`  -> The cheapest buying price seen on any previous day.
       * `max_profit` -> The biggest profit achieved so far.

   - On every single day `i` (where `i` is today's stock price):
       1. Calculate today's potential profit if we bought at `min_price` and 
          sold today (`curr_price = i - min_price`).
       2. Update `max_profit` if today's profit beats our best record so far.
       3. Update `min_price` if today's price is cheaper than our old lowest 
          price (so future days can use today as their buying day).

3. KEY "WHY" NOTES & EDGE CASES:
   - Why initialize `max_profit = 0`?
       * If prices strictly decrease every day (e.g., ``), every 
         `i - min_price` is negative or `0`. Starting `max_profit` at `0` 
         automatically guarantees we return `0` instead of a negative loss.
   - Why update `min_price` AFTER calculating `curr_price`?
       * Even if you updated `min_price` first, `i - i` would just equal `0`, 
         which never beats a positive `max_profit`. Still, checking profit first 
         makes the logic crystal clear: "Sell using past low, then record new low."
   - Variable Naming Tip:
       * In `for i in prices:`, `i` holds the actual stock price (not the index), 
         and `curr_price` actually represents `curr_profit` (today's profit).

4. COMPLEXITY ANALYSIS:
   - Time Complexity : O(n) -> Single pass through the `prices` array.
   - Space Complexity: O(1) -> Only two variables (`min_price`, `max_profit`) used.
================================================================================
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Start by assuming Day 0 is our cheapest buying price
        min_price = prices[0]
        # Default to 0 profit in case prices only go down
        max_profit = 0

        # Scan each daily stock price `i` from left to right
        for i in prices:
            # Profit if we bought at the lowest past price and sold today
            curr_price = i - min_price

            # Keep the highest profit seen so far
            max_profit = max(curr_price, max_profit)

            # Update the lowest buying price if today is cheaper
            min_price = min(min_price, i)

        return max_profit


# ==============================================================================
# LOCAL TEST CASES FOR REFERENCE
# ==============================================================================
if __name__ == "__main__":
    sol = Solution()

    # Case 1: Standard profit (Buy at 1 on Day 1, Sell at 6 on Day 4 -> Profit 5)
    print("Case 1  ->", sol.maxProfit())  # Expected: 5

    # Case 2: Descending prices (No profit possible -> Return 0)
    print("Case 2     ->", sol.maxProfit())     # Expected: 0

    # Case 3: Single day (Cannot buy and sell on different days -> Return 0)
    print("Case 3               ->", sol.maxProfit())               # Expected: 0
