# https://leetcode.com/problems/maximum-depth-of-binary-tree/


class TreeNode: 

	def __init__(self, val, left = None, right = None):

		self.val = val
		self.left = left
		self.right = right
	

def maxDepth_dfs(root):
	# one cons for this methods is that
	# there's a global variable right here to 
	# record but global is really nauty and we 
	# should try our best to avoid (solution: divide and conquer)
	if not root: return 0

	maxDepth, results = 0, []
	_dfs(root, maxDepth, results)
	return max(results)


def _dfs(root, maxDepth, results): 
	# 注意results 是个list 是mutable
	# 如果arguemnt 是一个string or integer
	# 他们是immutable 状态没法改变 (他们都描述的的是当前的那个level的状态)

	if not root: 
		results.append(maxDepth)
		return

	maxDepth += 1
	
	_dfs(root.left, maxDepth, results)
	_dfs(root.right, maxDepth, results)



def maxDepth_DQ(root):
	# bottom up (左右小弟将保护费上交)
	if not root: return 0

	left = maxDepth_DQ(root.left)
	right = maxDepth_DQ(root.right)

	# 整棵树的最大高度是左子树的高度 和 右子树的高度 中最大的 + 1
	return max(left, right) + 1


if __name__ == "__main__":
	#        1 
	#      /   \
	#     2     3
	#    / \   
	#   2   4 
	#  / 
	# 100

	root = TreeNode(val = 1)
	root.left = TreeNode(val = 2)
	root.right = TreeNode(val = 3)
	root.left.left = TreeNode(val = 2)
	root.left.left.left = TreeNode(val = 100)
	root.left.right = TreeNode(val = 4)

	print(maxDepth_dfs(root = root))