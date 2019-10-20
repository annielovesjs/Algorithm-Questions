
# calculator question 2
# given a string that represents an expression, return teh result of the expression
# guarantees:
# the only mathematical operators will be + and  *
#all nums will be positive single digit numbers ( 0 - 9)
# each pair of parentheses will eiyher have two numbers and a single operator or a single number

#encounter a closing bracket, pop until opening bracket, 
# perform the past three operations and add it back onto the stack


def calculator(str):
    stack = []
    result = 0
    currEl = ''
    op1 = None
    op2 = None
    op = None

    for char in str:
        if char == ")":
            currEl = stack.pop()
            while currEl != '(':
                if currEl == '*' or currEl == '+':
                    op = currEl
                elif op1 == None:
                    op1 = currEl
                else:
                    op2 = currEl
                currEl = stack.pop()
            if(op != None):
                if(op == '*'):
                    result = int(op1) * int(op2)
                else:
                    result = int(op1) + int(op2) 
                stack.append(result)
                if(len(stack) == 1):
                    return result
                op = None
                op2 = None
            else:
                stack.append(int(op1))
                if(len(stack) == 1):
                    return int(op1)
            op1 = None
        else:
            stack.append(char)

print(calculator('((1+2)*3)'))
print(calculator('(8*((2+4)*2))'))
print(calculator('(((((4)))+1))'))