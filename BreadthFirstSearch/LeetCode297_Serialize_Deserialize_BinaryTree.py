# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# see linear representation of binary tree explaintation: https://github.com/Jansonboss/LeetCoding/blob/main/BreadthFirstSearch/LeetCode102_TreeLevelOrder.py


class TreeNode:

	def __init__(self, val = None, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right


class Binary_Serialize_tool:

	def serialize(root):
		
		# root = [1, 2, 3, #, #, 4, 5]
		# this serailization is really clever we initlaize with our results list
		# with the first node of the root which is node(1) and then append its
		# left and right child to the results. we also use idx to work as stack
		# eg. [1, 2, 3, 4] => [1, 2, 3, 4]
		#	   ^			      ^  -> move idx to left = popleft of deque
		results, idx = [root], 0
		while idx < len(results): # for each level
			if results[idx]:
				results.append(results[idx].left)
				results.append(results[idx].right)
			idx += 1
		
		# remove "#" in the end
		while not results[-1]: results.pop()

		# return [i.val if isinstance(i, TreeNode) else "#" for i in results]
		return [i.val for i in results if isinstance(i, TreeNode) ]


	def deserialize(self, data):
		pass



if __name__ == "__main__":

	root = TreeNode(val = 1)
	root.left = TreeNode(val = 2)
	root.right = TreeNode(val = 3)
	root.right.left = TreeNode(val = 4)
	root.right.right = TreeNode(val = 5)

	print(Binary_Serialize_tool.serialize(root=root))