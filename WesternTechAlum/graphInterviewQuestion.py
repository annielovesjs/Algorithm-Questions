def isValidConfig(arr):
    graph = {}
    visited = {}
    recStack = {}
    vertices = set()

    for i in range(len(arr)):
        vertices.add(arr[i][0])
        vertices.add(arr[i][1])
        if arr[i][0] not in graph:
            graph[arr[i][0]] = [arr[i][1]]
        elif graph[arr[i][0]]: 
            graph[arr[i][0]].append(arr[i][1])    
    
        visited[arr[i][0]] = False
        visited[arr[i][1]] = False
        recStack[arr[i][0]] = False
        recStack[arr[i][1]] = False
    #traverse through the graph, if recstat = true (currently traversing the path for that node and then went back
    # and  visited = true 
    for vertex in vertices:
        if visited[vertex] == False:
            if checkCyclic(vertex, visited, recStack, graph):
                return False

    return True
def checkCyclic(node, visited, recStack, graph):
    visited[node] = True
    recStack[node] = True

    if node not in graph:
        return False
    for i in graph[node]:
        if visited[i] == False:
            if(checkCyclic(i, visited, recStack, graph)):
                return True
        elif recStack[i] == True:
                return True
        
    recStack[node] = False
    return False



print(isValidConfig([[1, 0], [0, 1]])) #should return false
print(isValidConfig([[1, 2], [1, 3], [3, 2]])) #should return false
print(isValidConfig([[1, 2], [1, 3], [3, 4]])) #should return true
print(isValidConfig([[1, 2], [3, 4]]))  #should return true
print(isValidConfig([['a', 'b'], ['b', 'c'], ['c', 'a']])) #should return falsez sf