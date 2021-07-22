# https://leetcode.com/problems/binary-tree-level-order-traversal/

# static array: tuple in python
# dynmaic array: list in python
# [1, 2, 3, _, _, _] every time you create a list, python will create a
# dynamic array so that you can do append later otherwise we need to 
# copy the  value of array which is inefficient

# queue 队列 we can use linked list to implement queue

#      ---------------
# <---				  <-----
#      ---------------



# dequeue  we can use doubly-linked list to implement queue

#      ---------------
# <--->			       <----->
#      ---------------
# 这题我们用dequeue因为当其为空时，我们pop就会报错然而queue pop的时候
# 会卡在哪里（多线程） 你也不知道为啥出错不好debug
# https://learnku.com/docs/pymotw/queue-thread-safe-fifo-queue/3370


# https://stackoverflow.com/questions/53923064/how-to-deal-with-null-in-python-list-leetcode-104
# Notice that this is seralized (linear description of tree)

# Input: root = [3,9,20,null,null,15,7] Output: [[3],[9,20],[15,7]]
# those 2 nulls're left and right child of 9
# 15 and 7 are left and right child of 20

# def levelOrder(root):
#    从i层拓展到i+1层 since ele in i+1 must be left and right child of ith, we can for loop it
#    while the node:	
#    for i level:
#        find i + 1 level 

from collections import deque

class TreeNode:

	def __init__(self, val = None, left = None, right = None):

		self.val = val
		self.left = left
		self.right = right
	
def levelOrderTraversal(root):
	# and we actually don't need queue check out serialize part lt297:
	# https://github.com/Jansonboss/LeetCoding/blob/main/BreadthFirstSearch/LeetCode297_Serialize_Deserialize_BinaryTree.py
	if not root: return []

	queue, results = deque([root]), []
	# while current level is not empty
	while queue:
		level = []
		print(len(queue))
		# 在当前层中去遍历每个变量
		# 第一层就一个变量，第二层有两个变量 depends on (len(queue)) etc。。
		for _ in range(len(queue)):
			node = queue.popleft() 
			level.append(node.val)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		results.append(level)
	return results


if __name__ == "__main__":

	root = TreeNode(val=1)
	root.left = TreeNode(val=2)
	root.right = TreeNode(val=3)
	root.right.left = TreeNode(val=4)
	root.right.right = TreeNode(val=5)
	# [1, 2, 3, null, null, 4, 5]
	#
	#               1
	#          /        \
	#        2            3
	#                  /     \ 
	#                 4       5
	print(levelOrderTraversal(root))
