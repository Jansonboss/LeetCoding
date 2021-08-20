# https://leetcode.com/company/bytedance/

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# using sorted to get common key

from collections import defaultdict

def groupAnagram(strs):
    
    if not strs: return None
    
    results, grouped = [], defaultdict(list)
    
    for word in strs:
        key = "".join(sorted(word))
        grouped[key].append(word)
    
    return list(grouped.values())

if __name__ == "__main__":
    print(groupAnagram(strs = ["eat","tea","tan","ate","nat","bat"]))