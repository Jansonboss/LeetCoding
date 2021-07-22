# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/


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
