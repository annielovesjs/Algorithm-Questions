# //Question 2: Satisfying subarrays
# //given an array, arr, and a value, k, return the number of subarrays
# //that can be made from arr which contains k odd numbers
# //ex. {1,2,3,4,5}, 2 -> 4
# //ex. {1,3,4,5}, 0 -> 1
# //ex. {1,4,6,8,10}, 1 -> 5

def numSubArray(arr, k):
    totalCount = 0
    numOdds = 0
    n = len(arr)
    prefix = [0] * n

    for i in range(n):
        prefix[numOdds] +=1
        if arr[i] % 2 != 0:
            numOdds += 1
        if numOdds >= k:
            totalCount += prefix[numOdds - k]

    return totalCount

print(numSubArray([1,2,3,4,5], 2 ))
print(numSubArray([1,3,4,5], 0))
print(numSubArray([1,4,6,8,10], 1))