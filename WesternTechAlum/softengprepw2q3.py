from collections import defaultdict
from collections import OrderedDict

class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count
    
class LFUCache(object):
    def __init__(self, size):
        self.size = size
        self.nodeKeys = {}
        self.nodeFrequencies = defaultdict(OrderedDict)
        self.minCount = None
        
    def get(self, key):
        if key not in self.nodeKeys:
            return -1
        
        node = self.nodeKeys[key]
        del self.nodeFrequencies[node.count][key]

        if not self.nodeFrequencies[node.count]:
            del self.nodeFrequencies[node.count]
        
        node.count += 1
        self.nodeFrequencies[node.count][key] = node
        
        if not self.nodeFrequencies[self.minCount]:
            self.minCount += 1
            
        return node.val
        
    def put(self, key, value):
        if not self.size:
            return 
        
        if key in self.nodeKeys:
            self.nodeKeys[key].val = value
            self.get(key) 
            return
        
        if len(self.nodeKeys) == self.size:
            k = self.nodeFrequencies[self.minCount].popitem(last=False) 
            del self.nodeKeys[k[0]] 
        
        self.nodeFrequencies[1][key] = self.nodeKeys[key] = Node(key, value, 1)
        self.minCount = 1
        return

cache = LFUCache( 2)

print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))      # returns 1
print(cache.put(3, 3))    #evicts key 2
print(cache.get(2))       #returns -1 (not found)
print(cache.get(3))       # returns 3.
print(cache.put(4, 4))    #evicts key 1.
print(cache.get(1))       #returns -1 (not found)
print(cache.get(3))       # returns 3
print(cache.get(4))      # returns 4