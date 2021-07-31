# https://leetcode.com/problems/coin-change/

# coin with worth 2, 5, 7 dollars ===> 27 dollars
# Find the combination that using the minimum number of coins
 
## Intuition: tried using the the most valued coin eg. 7
## 1. --> 7 + 7 + 7 + 5  = 26 but it is wrong since we need 1 more dollars

# STEP1. 确定状态 F(X) = min(F(x-2) + 1, F(x-5) + 1, F(x-7) + 1)

# - 1.1 define last step ak: if it is the optimized solution, 27 - ak( the last coin) must be the optimized solution as well -》 ( k -1 ) coins
# - 1.2 tansform to subproblem

# 动规语贪心的区别在于: 贪心是第一步不管三七二十一先将利益最大或最小化 （但是目光会比较狭窄断短浅因为有可能第一步就走错了）
# 而动规的思想在于：我们每一步都是根据之前的一步进行优化的 （每一步都是最优然后达成全局最优)
# 具体思想是 当我们到 27时，我们得在 （25， 22， 20）选个最小的 （然后 25， 22， 20中 他们分别在递归下去）
# 但是这样导致重复计算所以我们将算过的数值存在 dp array中 （其实非常类似dfs + memoization）
# 因为每一步都是根据之前的一步进行优化的，所以一个非常自然的想法就是自下而上（bottom up）

def coinChange(coins, amount):
	"""
	》》》 ----------------------------- 》》》》》》》》》 bottom up

	[INF, INF, INF,  0, INF, 1, INF, 2                             ]
	 -3,  -2,  -1,   0, 1,   2,  3,  4 , 5,  6 , 7,  8,  9 ....

	f(1) = min(f(1-2), f(1-5), f(1 - 7)) + 1 = min(inf, inf, inf) + 1 = inf + 1  = inf 
	# 没法用2， 5， 7 平凑出一块钱
	
	f(2)  = min(f(2-2), f(2-5), f(2 - 7)) + 1 = min(0, inf, inf) + 1 = 0 + 1  = 1 
		# 最少能用多少个coins平凑出两块钱 -》 1个

	f(3)  = min(f(3-2), f(3-5), f(3 - 7)) + 1 = min(inf, inf, inf) + 1 = INF + 1  = INF
	f(4)  = min(f(4-2), f(4-5), f(4 - 7)) + 1 = min(1, inf, inf) + 1 = 1 + 1  = 2
	"""
	if (not coins) and (not amount):
		return 0

	dp = [float("inf")] * (amount + 1)
	dp[0] = 0

	for i in range(1, amount + 1):
		for coin in coins:
			if ((i - coin) < 0):
				continue
			# state transform function f(x) = min(f[x-1]+1), f[x-5]+1, f[x-7]+1)
			dp[i] = min(dp[i-coin] + 1, dp[i])

	if dp[-1] == float('inf'): 
		return -1

	return dp[-1]


if __name__ == "__main__":
	print(coinChange(coins = [2, 5, 7], amount = 27))