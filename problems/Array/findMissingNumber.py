#How do you find the missing number in a given integer array of range
#input

number_list = [1,2,3,4,5,6,7,8,9,10,11,12,14,15]
#output 
#missing number 13

#using XOR
def find_missing_number(arr,n):
    x1 = arr[0]
    x2 = 1

    for i in range(1,n):
        x1 = x1^arr[i]
        print(x1, end=' ')
    print()
    
    for i in range(2, n+2):
           x2 = x2^i

    return x1^x2


result = find_missing_number((number_list), len(number_list))
print(result)
