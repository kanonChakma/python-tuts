nums = [3,4,5,62,1,4,5,6,7,8,1,3]
unique = []

for num in nums:
    if num in unique:
        print(num)
    else:
        unique.append(num)

print(unique)
