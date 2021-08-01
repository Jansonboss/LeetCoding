# https://leetcode.com/problems/jump-game/



def jumpGame(nums):

	if not nums: return None

	dp = [0] * len(nums)
	dp[0] = True

	# jth stone is the next stone of i
	for j in range(1, len(nums)):
		dp[j] = False
		# for each stone j, I need to check out
		# all the previous stones where
			# 1. whether the previous stone could be reached
			# 2. whether next jth stone could be reached from ith stone
		for i in range(j):
			if dp[i] and (i + nums[i] >= j):
				dp[j] = True
				break

	return dp[-1]

if __name__ == "__main__":
	print(jumpGame(nums = [3, 2, 1, 0, 4]))
	print(jumpGame(nums = [2, 3, 1, 1, 4]))