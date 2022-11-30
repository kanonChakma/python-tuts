#Time Complexity : O(n)
def reverse(arr, n):
    for i in range(n//2):
        temp = arr[i]
        arr[i] = arr[n-i-1]
        arr[n-i-1] = temp

    return arr

arr = [1,2,3,4,5,6,7,8]
result = reverse(arr, len(arr))
print(result)

#Time Complexity : O(n)
#Another Solution
def reverseList(arr, start, end):
    while start < end:
        arr[start],arr [end] =  arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr

arr = [1,2,3,4,5,6,7,8]
result = reverseList(arr, 0, len(arr)-1)
print(result)


#Time Complexity : O(n)
#Using recurison
def reverseList(arr, start, end):
    if start >= end:
        return

    arr[start],arr [end] =  arr[end], arr[start]
    reverseList(arr, start+1, end-1)
    
    return arr

arr = [1,2,3,4,5,6,7,8]
result = reverseList(arr, 0, len(arr)-1)
print(result)


#Using Python List slicing

def reverseList(A):
    print(A[::-1])


A = [1, 2, 3, 4, 5, 6]
print(A)
print("Reversed list is")
reverseList(A) 












