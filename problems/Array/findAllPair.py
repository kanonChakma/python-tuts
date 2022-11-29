#Input: 
arr = [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1] 
sum = 11
10,12,10,15,7,6,7,6,2,
1,1,1,1,1,1,1
#Output:  9

#first solution
# Time Complexity: O(n2), traversing the array for each element
# Auxiliary Space: O(1)
def find_all_pair(nums, length, sum):
    count = 0
    for i in range(length):
        for j in range(i+1, length):
            if nums[i]+nums[j] == sum:
                count+=1

    return count

result = find_all_pair(arr, len(arr), sum)
print(result)

#second solution
#using dictonary
def find_all_pair(nums,length,sum):
    dic = {}
    count = 0
    for num in nums:
        if dic.get(sum-num):
            count += dic[num]
        else:
            dic[num] = 1

    return count



result = find_all_pair(arr, len(arr), sum)
print(result)
