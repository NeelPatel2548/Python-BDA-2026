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


# # Loop through multiple arrays simultaneously with unpacking
# nums1 = [1, 3, 5]
# nums2 = [2, 4, 6]
# for n1, n2 in zip(nums1, nums2):
#     print(n1, n2)


# # Sorting
# arr = [5, 4, 7, 3, 8]
# arr.sort()
# print(arr)

# arr.sort(reverse=True)
# print(arr)


# **** Rule of thumb: If the function is just one simple expression, lambda is a good choice. If it needs multiple statements, loops, or conditions, use def.
# arr = ["me", "you", "he", "she", "it"]
# print(arr)

# arr.sort(key =lambda x: len(x))
# print(arr)


### Array multiplication
# a1 = [1, 2, 3]
# a2 = [4, 5, 6]

# for i in a1:
#     print("\n")
#     for j in a2:
#         print(i * j)




# | Method             | Purpose                                | Example                     |
# | ------------------ | -------------------------------------- | --------------------------- |
# | `append(x)`        | Add an element at the end              | `arr.append(10)`            |
# | `extend(iterable)` | Add multiple elements                  | `arr.extend([4, 5])`        |
# | `insert(i, x)`     | Insert at a specific index             | `arr.insert(1, 100)`        |
# | `remove(x)`        | Remove the first occurrence of a value | `arr.remove(5)`             |
# | `pop([i])`         | Remove and return an element           | `arr.pop()` or `arr.pop(2)` |
# | `clear()`          | Remove all elements                    | `arr.clear()`               |
# | `index(x)`         | Find the index of a value              | `arr.index(20)`             |
# | `count(x)`         | Count occurrences                      | `arr.count(5)`              |
# | `sort()`           | Sort the list                          | `arr.sort()`                |
# | `reverse()`        | Reverse the list                       | `arr.reverse()`             |
# | `copy()`           | Create a shallow copy                  | `new_arr = arr.copy()`      |
