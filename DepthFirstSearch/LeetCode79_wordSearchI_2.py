# https://leetcode.com/problems/word-search/ 
# This kind of queston is suitable for DFS since the lenghth of english word
# is somehow limited which means the depth of the recursion is limited as well

def findWord(board):
	"""
	find all the words in the board with adjacent letter 
	word length: 3 to 8 characters
	"""
	results, subset = set(), []
	visited = [[0] * len(board) for _ in range(len(board))]
	row, col = len(board), len(board[0])
	for i in range(row):
		for j in range(col):
			dfs(results, subset, i, j, board, visited, dx, dy)
	return results

def inbound(board, x, y):
	# check if it is inside the board
	if (0 <= y < len(board)) and (0 <= x < len(board[0])):
		return True

def dfs(results, subset, x, y, board, visited, dx, dy):

	if len(subset) == 8: 
		return

	if len(subset) >= 3:
		results.add("".join(subset))
	
	for n in range(len(dx)):
		_x = x + dx[n]
		_y = y + dy[n]

		visited[x][y] = 1 # no revisit
		subset.append(board[x][y])

		if (inbound(board, _x, _y)) and (not visited[_x][_y]):
			dfs(results, subset, _x, _y, board, visited, dx, dy)

		visited[x][y] = 0
		subset.pop() # backtracking


if __name__ == "__main__":

	dx = [1, -1, 0, 0, 1, -1, 1, -1]
	dy = [0, 0, 1, -1, 1, -1, -1, 1]

	BOARD = \
	    [
	        ["R", "A", "E", "L"],
	        ["M", "O", "F", "S"],
	        ["T", "E", "O", "K"],
	        ["N", "A", "T", "I"]
	    ]

	print(len(findWord(BOARD)))