#input
arr = [7, 10, 4, 3, 20, 15] 
k = 3 
#output 7

arr= [7, 10, 4, 3, 20, 15] 
k = 4
#output 10


#first solution
# Time Complexity: O(NlogN)
# Auxiliary Space: O(1)

arr.sort()
print(arr[k-1])






