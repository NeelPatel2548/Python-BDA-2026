#NeetCode

# arr = [1,2,3,4,5,6,7]

# print(arr[1:5])  # Output: 1

# # Unpacking
# a, b, c = [1, 2, 3]
# print(a, b)

# *** enumerate() is a built-in Python function that lets you loop over an iterable while also getting the index of each element.

# fruits = ["apple", "banana", "mango"]

# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# out: 
# 0 apple
# 1 banana
# 2 mango


# Loop through multiple arrays simultaneously with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)