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