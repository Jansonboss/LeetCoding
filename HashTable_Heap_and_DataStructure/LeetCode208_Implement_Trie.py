# https://leetcode.com/problems/implement-trie-prefix-tree/

# Good Resources:
# https://www.youtube.com/watch?v=pkaooVBexeU&ab_channel=%E5%B1%B1%E6%99%AF%E5%9F%8E%E4%B8%80%E5%A7%90
# https://www.youtube.com/watch?v=oobqoCJlHA0&t=664s&ab_channel=NeetCode

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# 			|          |        |
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
#           |         |         | 
# Output [null,     null,     true, false, true, null, true]

# explaination: first initialize Trie, insert apple and then search apple, and then search app



# notice that the insert and search could be donwe by using hash set
# why we bother using prefix tree? This is because we need the startwith
# methods (check prefix) we can loop over all the words and hashset all the
# prefix but there'll be lots of duplicayted character

# eg. applea, ape => {a, ap, app, appl, apple, a, ap, ape, } => prefix set (lots of a are duplicated)
#                         |   |    | 
#                    a, p, p are all repated
 
# While in Trie we can efficiently store the prefix
#                     	root                                   children1: dict()
# 					/                                         /
#                   ----------------------------------------/
# current -------> | a |   |   |   |    |   |  |   |   |   |
#                  -----------------------------------------
#                /       \
#       --------------    ---------------- ----> children1["a"]
#       |   | p  |    |   | r  |   |   |   | 
#        --------------   -----------------
#             /     \             \
#  -----------     ---------        ----------------------------
# |  |   | p |     |e  |  |        	| ....   |    | m  |   |   | 
#  -----------     ----------         ----------------------------
#        /

#       l
#      /
#     e

# 九章强化班: 要记住所有的tree都是由root组成的


class TrieNode:

	def __init__(self):
		self.isWord = False
		self.children = {}
	
class TrieTree:

	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		# 注意每次插入都是先生成空的dict然后在插入char
		curr = self.root
		for char in word:	
			if char not in curr.children:
				curr.children[char] = TrieNode()
			curr = curr.children[char] # <- 这里要小心别写成curr = curr.children
		return True
		curr.isWord = True
	
	def search(self, word):
		curr = self.root
		for char in word:	
			if char not in curr.children:
				return False
			#注意children是个set【a, b, c, ..., g...】然后 children[a] 是上面的字符
			# 你指针得指向那个children set里面的字符而不是这个children set
			curr = curr.children[char]
		return True

	def starWith(self, prefix):
		curr = self.root

		for char in prefix:
			if char not in curr.children:
				return False
			curr = curr.children[char] # <- 这里要小心别写错
		return True