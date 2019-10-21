#group anagrams problem
from collections import defaultdict

def groupAnagrams(strs):
    anagram_list = defaultdict(list)
    for str in strs:
        count = [0] * 26
        for char in str:
            count[ord(char) - ord('a')] +=1
        anagram_list[tuple(count)].append(str)
    return anagram_list.values()

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))