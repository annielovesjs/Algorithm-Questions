# //Question 1: Longest Alphabetical Substring
# //given a stirng, return the longest substring in which all characters are in Alphabetical order
# //ex. 'abfcj' -> 'abf'
# //ex. 'abaflmnoa' -> 'aflmno'
# //ex. 'zyma' -> 'z'

# //O(N), greedy approach
def longestSubstring(str):
    longestLength = 0
    currentStr = ''
    longestStr = ''
    currIdx = 0    

    while currIdx < len(str) :
        if currIdx == 0 :
            prevChar = str[currIdx]
            currentStr += str[currIdx]
        else: 
            if str[currIdx] > prevChar :
                currentStr+=str[currIdx]
            else :
                if longestLength < len(currentStr) :
                    longestLength = len(currentStr)
                    longestStr = currentStr
                currentStr = str[currIdx]
        prevChar = str[currIdx]
        currIdx+=1
    return longestStr
 


print(longestSubstring('abaflmnoa'))