# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Two pointer methods
def max_profit_two_pointers(nums):

	if not nums: return None

	left, right, max_profit = 0, 0, float("-inf")

	while left < len(nums) or right < len(nums):
		if nums[right] < left[left]:
			left = right
			right = right + 1
		else:
			profit = nums[right] - nums[left]
			max_profit = max(profit, max_profit)
			right += 1
	return max_profit



# dynamic programming methods
