# https://leetcode.com/problems/binary-tree-postorder-traversal/
# http://www.jiuzhang.com/solutions/binary-tree-postorder-traversal/

# 3 ways to postorder traversal the binary tree



# Tree Traversal
class TreeNode:

	def __init__(self, val, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right


## DFS + Recursion
def Postorder_traversal_Recur(root):
	# In DFS recursion traversal We don't return anything, we will save the
	# results inside the function parameter as global variable during the reeursion
	results = []
	_dfs_preorder_Recur(root, results)
	return results

def _dfs_preorder_Recur(root, results):
	
	if not root: return

	# inorder
	results.append(root.val)
	_dfs_preorder_Recur(root.left, results)
	_dfs_preorder_Recur(root.right, results)


## DFS + Divide + Conquer0
def PostOrder_Traversal_DQ(root):
	# for divide and conquer it is also the same with recursion
	# the only major diff is that DQ need to return the results
	# and we should not change the parameter of function
	# (Unlike the recursion) the only thing we wanna change and determine is the retuen
	# value of the function
	results = []

	if not root: return results
	
	# divide
	left = PostOrder_Traversal_DQ(root.left)
	right = PostOrder_Traversal_DQ(root.right)

	# conquer
	results.append(root.val)
	results.extend(left)
	results.extend(right)

	return results


## DFS + stack (recursion)
def PostOrder_Traversal_Stack(root):
	# same thing with BFS level order traversal
	if not root: return []

	stack, results = [root], []

	while stack:
		# tricky part here is that when append right later
		# rthe first thing we pop out is right which is since
		# the walker will walk to right instead of left
		# So we need to firstly append the right and then left
		node = stack.pop()
		if node.left:
			stack.append(node.right)
		if node.right:
			stack.append(node.left)
		results.append(node.val)
	return results



if __name__ == "__main__":
	#        1 
	#      /   \
	#     2     3
	#    / \   /  \
	#   2   4 

	root = TreeNode(val = 1)
	root.left = TreeNode(val = 2)
	root.right = TreeNode(val = 3)
	root.left.left = TreeNode(val = 2)
	root.left.right = TreeNode(val = 4)

	print(Postorder_traversal_Recur(root = root))
	print(PostOrder_Traversal_Stack(root = root))

	print(PostOrder_Traversal_DQ(root = root))