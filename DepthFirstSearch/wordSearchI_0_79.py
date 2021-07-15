# # https://leetcode.com/problems/word-search/ 

def findWord(board, word):
    if not board or not word: return False
    row, col = len(board), len(board[0])
    for y in range(row):
        for x in range(col):
            if _search(board, word, 0, x, y, row, col): 
                return True
    return False

def _outOfBound(x, y, row, col):
    if y < 0 or y == row or x < 0 or x == col:
        return True
    return False

def _search(board, word, idx, x, y, row, col):
	"""
    idx: nth idx of charator in word eg.TEA
    x, y: coordinates on the board
	"""
	if _outOfBound(x, y, row, col):
		return False

	if word[idx] != board[y][x]:
		return False

	if idx == len(word) - 1:
		return True

	current = board[y][x]
	board[y][x] = 0 # same cell cannot be revisted at current level

	found = \
		_search(board, word, idx + 1, x + 1, y, row, col) or \
		_search(board, word, idx + 1, x - 1, y, row, col) or \
		_search(board, word, idx + 1, x, y + 1, row, col) or \
		_search(board, word, idx + 1, x, y - 1, row, col)     

	board[y][x] = current # backtracking
	return found


if __name__ == "__main__":

	VALID_ANSWER = ["TEA","EAT","ARM", "KIT", "FEAR"]
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