# software eng prep interview question set 3
#q1
def wordReconstruction(arr):
    neighbours = {}
    parentDep = {}
    visited =  {}

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            visited[arr[i][j]] = False
            if j == 0:
                if arr[i][j] not in parentDep:
                    parentDep[arr[i][j]] = 0
            else:
                lastChar = arr[i][j-1]
                currChar = arr[i][j]

                if currChar not in parentDep:
                    parentDep[currChar] = 1
                else:
                    parentDep[currChar] += 1
                
                if lastChar not in neighbours:
                    neighbours[lastChar] = [currChar]
                elif neighbours[lastChar] and currChar not in neighbours[lastChar]:
                    neighbours[lastChar].append(currChar)
    stack_1 = []
    stack_2 = []
    final_str = ''
    for key, value in parentDep.items():
        if value == 0:
            stack_1.append(key)
    stack_2 = dfs_helper(neighbours, stack_1, stack_2, visited, stack_1[len(stack_1)-1])
    while len(stack_2) != 0:
        final_str+= stack_2.pop()
    return final_str

def dfs_helper(childList, stack_1, stack_2, visited, node):
    if len(stack_1) == 0:
        return stack_2
    if node not in childList:
        node = stack_1.pop()
        stack_2.append(node)
        return stack_2
    node = stack_1[len(stack_1)-1]
    for i in childList[node]:
        if not visited[i]:
            stack_1.append(i)
            visited[i] = True
            stack_2 = dfs_helper(childList, stack_1, stack_2, visited, i)
    node = stack_1.pop()
    stack_2.append(node)
    return stack_2


print(wordReconstruction(['bs3', 'wb3', 'wba', 'as3f']));  
print(wordReconstruction(['af', 'ag']))              




#q2 Tree reconstruction
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    
class Counter:
    def __init__(self):
        self.val = 0
    def incrementCount(self):
        self.val += 1
    def getCount(self):
        return self.val

def buildTree(preorder, inorder):
    dict = {}
    counter = Counter()
    left = 0
    right = len(inorder) - 1
    for i in range(len(inorder)):
        dict[inorder[i]] = i
    return buildTreeHelper(preorder, dict, left, right, counter)

def buildTreeHelper(preorder, inorderDict, left, right, counter):
    if counter.getCount() > right + 1:
        return
    node = preorder[counter.getCount()]
    counter.incrementCount()
    root = TreeNode(node)
    root_idx = inorderDict[node]
    if root_idx != left:
        root.left = buildTreeHelper(preorder, inorderDict, left, root_idx-1, counter)
    if root_idx != right:
        root.right = buildTreeHelper(preorder, inorderDict, root_idx + 1, right, counter)
    return root

def printpreOrderTraversal(tree):
    if not tree:
        return
    print(tree.value)
    printpreOrderTraversal(tree.left)
    printpreOrderTraversal(tree.right)
newTree = buildTree('MLZCWJEOK', 'ZCLJWMEKO')
printpreOrderTraversal(newTree)

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