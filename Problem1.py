
# Given a list of n-1 integers and these integers are in the range of 1 to n. 
# There are no duplicates in list. One of the integers is missing in the list. 
# Write an efficient code to find the missing integer. 

# Space complexity: O(1)
# Time complexity: O(log n)

def solution(arr):
    n = len(arr)
    low, high = 0, n - 1
    if arr[0] != 1:
        return 1
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] - mid == 2 and (mid == 0 or arr[mid-1] != 2):
            return mid + 1
        if arr[mid] - mid > 1:
            high = mid
        else:
            low = mid+1
    return -1

print(solution([1,2,3,5]))