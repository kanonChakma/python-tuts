#for sorted array
#Input arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
#Output {1, 2, 3, 4, 5}

def remove_duplicates(nums, n):
    if n==0 or n==1:
        return n
    temp = []

    for i in range(0, n-1):
        if nums[i] != nums[i+1]:
            temp.append(nums[i])

    temp.append(nums[-1])
    return temp

#better approach than previous
#it takes average O(1) look up in set
#space complexity is O(N)

def remove_duplicates(nums, n):
    seen = set()
    temp = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            temp.append(num)
            
    return temp


arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
arr = [2,2,2,2,2,2,2,2,2,2,2,2,2]
length = len(arr)
res = remove_duplicates(arr, length)
print(res)

#
a = [0,1,2,3,4,3,3,4]     
a = list(set(a))
print(a)

  
#https://stackoverflow.com/questions/64020727/better-solution-for-removing-duplicates-from-a-python-list
