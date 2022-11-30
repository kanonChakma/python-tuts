# Input: {2, 10,10, 100, 2, 10, 11,2,11,2}
# Output: 2 10 11

#first method
# Time Complexity: O(N2) 
# Auxiliary Space: O(N)
def find_duplicates(nums, length):
    res = []
    for i in range(length):
        for j in range(i+1, length):

            if nums[i] == nums[j]:
                if nums[i] in res:
                    break
                else:
                    res.append(nums[i])
    if(len(res)):
        return res
    else:
        return ("There is no duplicate")


nums = [2, 10,10, 100, 2, 10, 11,2,11,2]
nums = [5, 40, 1, 40, 100000, 1, 5, 1]
#nums = [4,5,6,7]
length = len(nums)

result = find_duplicates(nums, length)
print(result)


#second method
#using dictionary approach
# Time Complexity: O(N)
# Auxiliary Space: O(N)
def find_duplicates1(nums, n):
    dic = {}
    for i in range(n):
        if nums[i] in dic:
            dic[nums[i]]+=1
        else:
            dic[nums[i]] = 1
    
    for item in dic:
        if dic[item] >1:
            print(item, end=' ')
    print()


length = len(nums)
find_duplicates1(nums, length)

