# the standard way is to usef dfs + trie
# here we can also use hashmap (prefix set) to stop
# as long as current search char in not in the prefixt set
# This is exactly the same logic of prefic tree

# This is exactly the same with WordSearch2 prefix, on;y difference is that
# we need change the value of board and recover it back when backtracing rather than using visited array

def wordSearch2(board, words):

	if (not board) or (not words): return []

	row, col = len(board), len(board[0])
	visited = [[0] * col for _ in range(row)]
	results = []

	# preprocessing: store all the prefix
	prefix_set = set()
	for word in words:
		for i in range(len(word)):
			prefix_set.add(word[:i+1])
	# hash map words array as well since we need to frequently check
	word_set = set(words)

	# walking randomly on the board, and set start point to move
	for i in range(row):
		for j in range(col):
			# don't forget initilize the subset are first
			subset = list(board[i][j])
			_dfs(
				board, i, j, visited, results, subset,
				prefix_set, word_set
			)
	return results

def inbound(board, x, y):
	row, col = len(board), len(board[0])
	if (0 <= x < row) and (0 <= y < col):
		return True 

def _dfs(board, x, y, visited, results, subset, prefix_set, word_set):
	# don't forget initilize the subset with board[i][j] are first
	# otherwise uf subset is an empty list, it cannot pass the filter downbelow
	if "".join(subset) not in prefix_set:
		return

	if "".join(subset) in word_set:
		results.append("".join(subset))
		# don't return since there might be some words are prefix of another
		# eg. [eat, eater] if return we gonna just stop at eat and only found eat 

	dx = [-1, 1, 0, 0]
	dy = [ 0, 0, -1, 1]

	for n in range(len(dx)):
		x_, y_ = x + dx[n], y + dy[n]			

		if not inbound(board, x_, y_): continue

		# if visited[x_][y_]:
			# continue
		char = board[x_][y_]
		
		if board[x_][y_] == "#": continue
		
		# visited[x_][y_] = 1
		subset.append(board[x_][y_]) # be careful don't put board[x_][y_] = "#"aboe this line
		# otherwise subset will append # into itself
		board[x_][y_] = "#"
		_dfs(
			board,
			x_,
			y_,
			visited,
			results,
			subset,
			prefix_set,
			word_set
		)

		board[x_][y_] = char # recover previoud senerio
		subset.pop() # backtracking


if __name__ == "__main__":
	board = [
		["o","a","a","n"],
		["e","t","a","e"],
		["i","h","k","r"],
		["i","f","l","v"]
	]
	words = ["oath","pea","eat","rain"]
	print(wordSearch2(board=board, words=words))