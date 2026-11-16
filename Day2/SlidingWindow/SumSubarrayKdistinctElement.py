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
        