# https://leetcode.com/problems/longest-common-prefix/

class TrieNode:

	def __init__(self):
		self.children = {}
		self.isWord = False

class TrieTree:

	def __init__(self):
		self.root = TrieNode()
	
	def insert(self, word):
		curr = self.root
		for char in word:
			if char not in curr.children:
				curr.children[char] = TrieNode()
			curr = curr.children[char]
		curr.isWord = True
	

def longsetCommonPrefix(strs):
	tree = TrieTree()
	for word in strs: 
		tree.insert(word)
	
	curr, common_prefix = tree.root, []
	while not curr.isWord:
		# no divergence
		if len(curr.children) != 1:
			return "".join(common_prefix)
		
		prefix = next(iter(curr.children))
		common_prefix.append(prefix)
		curr = curr.children[prefix]

	return "".join(common_prefix)

if __name__ == "__main__":
	strs = ["flower","flow","flight"]
	print(longsetCommonPrefix(strs))
	strs = ["dog","racecar","car"]
	print(longsetCommonPrefix(strs))

	strs = ["apple","append","appl"]
	print(longsetCommonPrefix(strs))