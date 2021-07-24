# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# same thing with level order traversal 1 just use queue for results
# and append to the left


# https://stackoverflow.com/questions/53923064/how-to-deal-with-null-in-python-list-leetcode-104
# Notice that this is seralized (linear description of tree)

# Input: root = [3,9,20,null,null,15,7] Output: [[3],[9,20],[15,7]]
# those 2 nulls're left and right child of 9
# 15 and 7 are left and right child of 20

# [1, 2, 3, null, null, 4, 5]
#
#               1
#          /        \
#        2           3
#     /    \      /     \ 
#  null   null   4       5

class TreeNode:

	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def LevelOrderTraversal2(root):

	if not root: return []

	from collections import deque 
	queue, results = deque([root]), deque([])
	
	
	while queue:
		level = []
		for _ in range(len(queue)):
			node = queue.popleft()
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
			level.append(node.val)
		results.appendleft(level)	
	return list(results)
			
if __name__ == "__main__":

	root = TreeNode(val=1)
	root.left = TreeNode(val=2)
	root.right = TreeNode(val = 3)
	root.right.left = TreeNode(val = 4)
	root.right.right = TreeNode(val = 5)

	print(LevelOrderTraversal2(root))
