# https://leetcode.com/problems/binary-tree-preorder-traversal/



# https://leetcode.com/problems/binary-tree-preorder-traversal/solution/

# Awesome Video Tutorial
# https://www.youtube.com/watch?v=pUSy6UZCFKw&t=559s&ab_channel=DEEPTITALESRA

#                   1
#               /      \ 
#             2         3 
#          /    \     /   \
# #      4      5    6     7  


class TreeNode:

	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
	

def preOrderTraversal(root):
	if not root: return []

	stack, results = [root, ], []
	while stack:
		root = stack.pop()
		if root:
			results.append(root.val)
			# notice that here since we are doing preorder root->left->right, and since
			# we're using stack [left, right] if we pop right, we gonna traverse the child
			# nodes of right which is not correct: so we need to append right and then left1
			if root.right:
				stack.append(root.right)
			if root.left:
				stack.append(root.left)
			
	return results



if __name__ == "__main__": 
	# root = [1, null, 2, 3]

	#          1
	#       /     \
	#      #      2
	#           / 
	#          3

	root = TreeNode(val=1)
	root.left = TreeNode(val=None)
	root.right = TreeNode(2)
	root.right.left = TreeNode(3)
	print(preOrderTraversal(root))