# https://leetcode.com/problems/coin-change/


# coin with worth 2, 5, 7 dollars ===> 27 dollars
# Find the combination that using the minimum number of coins



## Intuition:
## tried using the the most valued coin eg. 7
## 1. --> 7 + 7 + 7 + 5  = 26 but it is wrong since we need 1 more dollars

# 1. 确定状态 F(X) = min(F(x-2) + 1, F(x-5) + 1, F(x-7) + 1)


def coinChange(coins, amount):

	if (not coins) or (not amount): return -1

	dp = ["INF"] * len(amount) + 1
	dp[0] = 0

	for i in range(1, amount + 1):
		for coin in coins:
			if (i >= coins) and (dp[i-coin] != "INF"):
				dp[i] = min(dp[i], dp[i-coin] + 1)
	
	if dp[amount] == "INF":
		return -1
	
	return dp[amount]