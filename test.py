numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45]
target = 35

right = len(numbers) - 1
left = 0 
mid_float = (right + left) / 2
mid = int(mid_float)
print(numbers[mid]) 
print(mid)

right = len(numbers) - 1
left = mid + 1      
mid_float = (right + left) / 2
mid = int(mid_float)
print(numbers[mid]) 

