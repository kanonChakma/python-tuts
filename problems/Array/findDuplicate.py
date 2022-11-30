#ind the duplicate number on a given integer array?
ages = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#time complexty is O(n^2)
def find_duplicate(nums, length):
    for i in range(length):
        for j in range(i+1, length):
            if(nums[i] == nums[j]):
                return True
    
    return False

#can be find first sort then check element 
#here time complxity will be O(nlogon) 
#space complexity will be O(1)


#using set
def find_duplicate(nums, length):
    return len(set(nums)) == len(nums)
    temp = set(nums)


#using hashmap
#time complexity is 0(N) 
#space complexity is O(N)

def find_duplicate(nums, length):
    temp = {}
    for num in nums:
        if num in temp:
            return True
        else:
            temp[num] = 1
    
    return False


#Optimal Solution
#Linked List cycle methods
# Time Complexity: O(n),
# Auxiliary Space: O(1),

def find_duplicate(nums):
    slow, fast = 0, 0
    check = 0

    #cyclick detection
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    while True:
        slow = nums[slow]
        check = nums[check]

        if slow == check:
            break
    
    return check


def find_duplicate(nums, length):
    if len(nums)< 1:
        return -1

    slow = nums[0]
    fast = nums[1]

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    fast = 0
    while fast != slow:
        fast = nums[fast]
        slow = nums[slow]
    
    return slow


length = len(ages)
res = find_duplicate(ages)

print(res)



 































