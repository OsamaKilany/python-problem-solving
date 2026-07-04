def sum_array(arr):
    if not arr or len(arr)==1: return 0
    i = 0
    for x in range(len(arr)):
        i+=arr[x]
    return i - max(arr) - min(arr)
        
arr = [1,2,3,4,5,6,7,8]
print(sum_array(arr))