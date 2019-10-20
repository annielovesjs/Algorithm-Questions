# Implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by 
# as many numerical digits as possible, and interprets them as a numerical value.
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
# [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or 
# INT_MIN (−231) is returned.


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = 1
        base = 0
        pointer = 0
        if len(str) == 0:
            return 0
        while pointer < len(str) -1 and str[pointer] == ' ':
            pointer+=1

        if str[pointer] == '+' or str[pointer] == '-':
            if str[pointer] == '-':
                sign = -1
            pointer+=1
        elif str[pointer] < '0' or str[pointer] > '9':
            return 0

        while pointer < len(str) and str[pointer] >= '0' and str[pointer] <= '9':
            if (base > (2**31 - 1) / 10) or (base == (2**31 - 1) / 10 and int(str[pointer]) > 7):                
                if sign == -1:
                    return (2**31) * -1
                else:
                    return (2**31) - 1
            #str - '0' returns the integer value of the curr item
            base = base * 10 + int(str[pointer])
            pointer+=1
        return sign * base
            
        
