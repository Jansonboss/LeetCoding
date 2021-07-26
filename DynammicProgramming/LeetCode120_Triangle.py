# https://leetcode.com/problems/triangle/


# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:

#					     2
#                      /   \
#					  3     4
#                    /  \  /  \ 
#				    6    5     7
#                 /   \  /  \  /  \  
#  	  	        4     1     8     3

# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

########## DFS: Cons: global variable: best and repeated calculation | O(2**n)
def miniumTotal_dfs(traingle):
	if not traingle: 
		return None

	# https://codereview.stackexchange.com/questions/43902/depth-first-search-use-of-global-variables-and-correctness-of-time
	best = [99999] # this is confusing to me 
	x, y, mysum, height= 0, 0, 0, len(traingle)
	_dfs(traingle, x, y, mysum, height, best)
	return best

def _dfs(traingle, x, y, mysum, height, best):
	if not traingle: return None

	if (x == height):
		best[0] = min(mysum, best[0]) # # this is confusing to me 
		return

	directions = [(1, 0), (1, 1)]

	for (dx, dy) in directions:
		_x, _y = x + dx, y + dy
		_dfs(traingle, _x, _y, mysum + traingle[x][y], height, best)


########## Divide and Conquer: pros: no global variable | O(2^n)

def miniumTtoal_DQ(traingles):
	if not traingles: return []

	return divideConquer(traingles, 0, 0)

def divideConquer(traingles, x, y):
	if x == len(traingles):
		return 0

	left = divideConquer(traingles, x + 1, y)
	right = divideConquer(traingles, x + 1, y + 1)
	return min(left, right) + traingle[x][y]


if __name__ == "__main__":
	traingle =  \
		[
			[2],          # (0, 0)
			              #    |   \ 
			[3, 4],       # (1, 0), (1, 1)
			              #    |   \  	/  \  
			[6, 5, 7],    # (2, 0), (2, 1), (2, 2)
			 			  #    |   \   |   \   |   \ 
			[4, 1, 8, 3]  # (3, 0), (3, 1), (3, 2), (3, 3)
		]
	
	print(miniumTotal_dfs(traingle=traingle))