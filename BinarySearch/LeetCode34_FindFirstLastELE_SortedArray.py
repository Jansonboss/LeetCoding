# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# uses binary search for two times
def searchRange(nums, target):


	if not nums: return [-1, -1]
	start, end = 0, len(nums) - 1
	left, right = -1, -1

	while start + 1 < end:
		mid = (start + end) // 2
		if nums[mid] <= target:
			start = mid
		else:
			end = mid

	if nums[start] == target:
		right = start
	if nums[end] == target:
		right = end


	start, end = 0, len(nums) - 1
	while start + 1 < end:
		mid = (start + end) // 2
		if nums[mid] >= target:
			end = mid
		else:
			start = mid

	if nums[end] == target:
		left = end
	if nums[start] == target:
		left = start

	return [left, right]