#q3 inflection point
# time complexity: O(log(n))
import math 
#store the prev number and compare 

def findInflection(arr):
    start = 0
    end = len(arr) - 1
    mid = math.floor((start + end) / 2)
    midLeft = mid - 1
    midRight = mid + 1

    if len(arr) <= 1 :
        return arr[0]
    
    else:
        while not mid >= end and not mid <= start:
            if arr[midRight] > arr[mid]:
                start = midRight
                mid = math.floor((start + end) / 2 )
            elif arr[midRight] < arr[mid]:
                if arr[midLeft] < arr[mid]:
                    return arr[mid]
                elif arr[midLeft] > arr[mid]:
                    end = midLeft
                    mid = math.floor((start + end) / 2)
            midLeft = mid - 1
            midRight = mid + 1 
        
        if arr[start] > arr[end]:
            return arr[start]
        return arr[end]
#test cases
print(findInflection([0, 1, 2, 8, 45, 90, 100, 321, 98, 47, -6, -200]))
print(findInflection([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
print(findInflection([1, 100, 200, 9]))
print(findInflection([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 1]))