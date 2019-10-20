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