"""
================================================================================
DSA STUDY JOURNAL — MAXIMUM NUMBER OF MONSTERS THAT CAN BE DEFEATED (GREEDY)
================================================================================

1. PROBLEM STATEMENT & GOAL:
   - You start with an initial experience level `e`, and there are `n` monsters.
   - Each monster `i` requires at least `power[i]` experience to defeat (`e >= power[i]`).
   - Defeating monster `i` rewards you with `bonus[i]` extra experience (`e += bonus[i]`).
   - You can fight the monsters in ANY order you want.
   - Goal: Return the MAXIMUM number of monsters you can defeat before getting 
     blocked by a monster stronger than your current experience.

2. CORE INTUITION ("GREEDY — FIGHT WEAKEST MONSTERS FIRST"):
   - Since you are allowed to choose the battle order, you should ALWAYS fight 
     the monster with the LOWEST `power` requirement first!
   - Why Greedy works here:
       * Every monster you defeat only INCREASES your experience (`bonus >= 0`).
       * Defeating weaker monsters early builds up your experience pool so you 
         become strong enough to defeat tougher monsters later.
       * If you cannot defeat the weakest remaining monster (`p > e`), you cannot 
         defeat ANY of the remaining stronger monsters either—so you stop immediately (`break`).

3. KEY PYTHON MECHANICS & "WHY" NOTES:
   - Why `monsters = list(zip(power, bonus))`?
       * `power` and `bonus` live in two separate lists. If you sorted `power` 
         alone, the powers would detach from their matching bonuses!
       * `zip(power, bonus)` glues each `(power[i], bonus[i])` together into a 
         paired tuple so they travel together when sorted.
   - How `monsters.sort()` sorts tuples in Python:
       * Python sorts tuples by their FIRST element (`power`) in ascending order 
         from smallest to largest.
       * If two monsters have the exact same `power`, Python automatically breaks 
         the tie using the SECOND element (`bonus`) in ascending order.
   - Why `if p > e: break`?
       * Because `monsters` is sorted by power, the very first time a monster's 
         power `p` exceeds your current experience `e`, every monster after it 
         will also have power `>= p > e`. No further fights are possible.
   - Competitive Programming Input Tip:
       * Notice that `input("no of monsters:")` prints prompt text. On online 
         judges (HackerRank, Codeforces, Infosys), use empty `int(input())` 
         without prompt strings so extra text isn't printed to stdout.

4. COMPLEXITY ANALYSIS:
   - Time Complexity : O(n log n) -> Sorting the `n` monster tuples dominates 
                                     the single O(n) battle loop.
   - Space Complexity: O(n)       -> Storing the paired `monsters` list of size `n`.
================================================================================
"""

# Read total monsters `n` and starting experience `e`
n = int(input("no of monsters:"))
e = int(input("starting exp:"))

power = []
bonus = []

# Read power required for each monster
for i in range(n):
    power.append(int(input("enter power:")))

# Read bonus experience rewarded by each monster
for i in range(n):
    bonus.append(int(input("enter bonus:")))

# Pair each monster's (power, bonus) together so sorting keeps them matched
monsters = list(zip(power, bonus))

# Greedy Step: Sort monsters in ascending order of required `power`
monsters.sort()

count = 0

# Fight monsters from weakest to strongest
for p, b in monsters:
    # If even the weakest remaining monster is stronger than current exp, stop!
    if p > e:
        break
    
    # Defeat the monster, absorb its bonus exp, and increment kill count
    e += b
    count += 1

print(count)


# ==============================================================================
# QUICK DRY-RUN TRACE EXAMPLE (FOR REFERENCE)
# ==============================================================================
# Input:
#   n = 3, e = 100
#   power = [101, 100, 304]
#   bonus = [100, 1, 524]
#
# Trace:
#   1. Paired & Sorted `monsters` -> [(100, 1), (101, 100), (304, 524)]
#   2. Fight (100, 1)   -> 100 <= 100 (Win!) -> e = 101, count = 1
#   3. Fight (101, 100) -> 101 <= 101 (Win!) -> e = 201, count = 2
#   4. Fight (304, 524) -> 304 > 201  (Lose -> break!)
#   Output: 2
