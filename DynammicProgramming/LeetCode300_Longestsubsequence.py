# https://leetcode.com/problems/longest-increasing-subsequence/

def lengthOdLS(nums):

	if not nums: return None

	dp = [1] * (len(nums) - 1)
	for i in range(0, len(nums)):
		for j in range(0, i):
			if nums[i] > nums[j]:
				dp[i] = max(dp[i], dp[j+1])
	return max(dp)