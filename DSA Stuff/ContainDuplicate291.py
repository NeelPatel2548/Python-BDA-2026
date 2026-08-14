class Solution:
    def hasDuplicate(self, nums):
        count = 0

        for i in range(1, len(nums) + 1):
            for j in range(i):
                print(nums[j], end=" ")
            print()

sol = Solution()
list = [10,2,3,4]
sol.hasDuplicate(list)
