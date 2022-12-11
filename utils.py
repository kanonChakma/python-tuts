#import Exercise.findMaximum
#from findMaximum import findMaximum
from Exercise.findMaximum import find_maximum

result = find_maximum([2,3,5,67,8])
print(result)


arr = [2,3,4,5,6]
arr2 = arr

print(arr2)

arr2[2] = 200

arr2 = [0] * 10
arr2[2] = 24

print(arr, arr2)

