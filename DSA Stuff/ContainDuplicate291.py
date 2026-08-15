#not fisible:

# class Solution:
#     def hasDuplicate(self, nums):
        # nums.sort()
# #         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 return True
#             return False

# sol = Solution()
# list = [10,2,10,3,4, 10]
# sol.hasDuplicate(list)



#besdt and optimal
#HashSet solution

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         seen = set() # tracks every digit we have seen
        
#         for num in nums:
#             if num in seen:
#                 return True
#             else:
#                 seen.add(num)
            
#         return False