# https://leetcode.com/problems/word-search/ 

def findWord(board, word):
	"""
	:type board: List[List[str]]
	:type word: str
	:rtype: bool
	"""
	dx = [1, -1, 0, 0]
	dy = [0, 0, 1, -1]
	
	row, col = len(board), len(board[0])
	results, subset, startIdx = [], [], 0
	visited = [[0] * col for _ in range(row)]
	
	for i in range(row):
		for j in range(col):
			if dfs(results, subset, board, word, i, j, startIdx, dx, dy, visited):
				return True                
	return False

def inbound(board, x, y):
	if (0 <= x < len(board)) and (0 <= y < len(board[0])):
		return True
	
def dfs(results, subset, board, word, x, y, idx, dx, dy, visited):
	
	if board[x][y] != word[idx]:
		return False
	
	if idx == len(word) - 1:
		return True

	# temp = visited[x][y]
	# visited[x][y] = temp
	
	for n in range(len(dx)):
		_x = x + dx[n]
		_y = y + dy[n]

		temp = visited[x][y]
		visited[x][y] = temp

		if (inbound(board, _x, _y)) and (not visited[_x][_y]):
			if dfs(results, subset, board, word, _x, _y, idx + 1, dx, dy, visited):
				return True
	
		visited[x][y] = temp
	return False


if __name__ == "__main__":
	print("hello")
	VALID_ANSWER = ["REA","TEA","EAT","ARM", "KIT", "FEAR"]
	INVALID_ANSWER = ["APPLE", "SIRI", "FOEAK"]

	BOARD = \
	[
		["R", "A", "E", "L"],
		["M", "O", "F", "S"],
		["T", "E", "O", "K"],
		["N", "A", "T", "I"]
	]

	# check valid answer
	print("Valid answer")
	for answer in VALID_ANSWER:
		print(answer, findWord(BOARD, answer))
	print("\n")

	# check invalid answer
	print("Invalid answer")
	for answer in INVALID_ANSWER:
		print(answer, findWord(BOARD, answer))