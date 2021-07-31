# https://leetcode.com/problems/unique-paths/

#   | 0  |  1 |  2 |  3 | 4 | 5 | 6 | 7 |
# --------------------------------------
# 0 |    |    |    |    |   |   |   |   |
# --------------------------------------
# 1 |    |    |    |    |   |   |   |   |
# --------------------------------------
# 2 |    |    |    |    |   |   |   |   |
# --------------------------------------
# 3 |    |    |    |    |   |   |   |   |
# --------------------------------------

def unique_path(m, n):
	if (not m) or (not n):
		return 0
	
	dp = [[0] * n for _ in range(m)]

	for i in range(m):
		for j in range(n):
			if (i == 0) or (j == 0):
				print(i, j)
				dp[i][j] = 1
				continue
			# there will be no negative idx since continue
			dp[i][j] = dp[i-1][j] + dp[i][j-1]

	return dp[m-1][n-1]



if __name__ == "__main__":
	print(unique_path(m = 3, n = 2))

			




