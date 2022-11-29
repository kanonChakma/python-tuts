arr = [5677856, 657856745356587687698768, 67564, 45675645356576578564435647647,4567564535657657, 8564435647647]

#first method
#Timecomlexity 0(nlogn)
# arr.sort()
# print(arr[0], arr[-1])

#second method 
#time complexity is O(n)
#space is O(1)

def find_min_max(nums):
    min = arr[0]
    max = arr[0]
    
    for num in nums:
        if num < min:
            min = num

        if num > max:
            max = num
    
    return [max,min]

result = find_min_max(arr)
print(result)

#third method using built in funciton called Min and Max
print([max(arr), min(arr)])
