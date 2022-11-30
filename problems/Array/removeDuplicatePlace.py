#Time Complexity : O(n) 
#Auxiliary Space : O(1)

def removeDuplicate(nums, len):
    l = 1
    for r in range(1,len):
        if nums[r] != nums[r-1]:
           nums[l] = nums[r]
           l+=1

    print(nums)
    return l

arr = [0,1,2,3,4,4,4,5,5,5,5,6,7]
# arr = [0,0,1,1,1,2,2,3,3,4]

result = removeDuplicate(arr, len(arr))
print(result)
print(arr)
