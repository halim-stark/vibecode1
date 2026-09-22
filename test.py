# numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45]
# target = 5

# right = len(numbers) - 1
# left = 0

# while left <= right:
#     mid = 0

#     midt = (left + right) // 2

#     if numbers[mid] == target:
#         final = numbers[mid]
#         break

#     elif numbers[mid] < target:
#         left = mid + 1
#         mid = (left + right) // 2
#         final = numbers[mid]

#     elif numbers[mid] > target:        
#         left = 0
#         right = mid - 1
#         mid = (left + right) // 2
#         final = numbers[mid]
# print(final)



# stack = []
# stack.append("A")
# stack.append("B")
# stack.append("C")

# hasil = stack.pop()

# print(hasil)
# print(stack)


from collections import deque

queue = deque()

queue.append("Python")
queue.append("Git")
queue.append("GitHub")
queue.append("DSA")

hasil1 = queue.popleft()
hasil2 = queue.popleft()
hasil3 = queue.popleft()
print(hasil1)
print(hasil2)
print(hasil3)
print(queue)



                     