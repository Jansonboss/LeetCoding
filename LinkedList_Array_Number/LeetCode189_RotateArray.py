# https://www.youtube.com/watch?v=BHr381Guz3Y&ab_channel=NeetCode
# 三步反转法
# [1, 2, 3, 4, 5] k = 2 ===> [4, 5, 1, 2, 3]
# Step 1: reverse=> [5, 4, 3, 2, 1]
# Step 2: reverse [:k] and [k:] => [5, 4, |||  3, 2, 1 ] => [4, 5, ||| 1, 2, 3]


def _reverse(nums, l, r):
	if not nums: return None
	
	while l < r:
		nums[l], nums[r] = nums[r], nums[l]
		l, r = l + 1, r - 1

def rotate_array(nums, k):

	if (not nums) or (not k): return []
	if k >= len(nums): return nums

	# Step 1 reverse whole list
	_reverse(nums=nums, l = 0, r = len(nums)-1)

	# step 2 reverse 1st portion
	_reverse(nums, l = 0, r = k-1)

	# step 3 reversse 2nd portion
	_reverse(nums, l = k, r = len(nums)-1)
	return nums


if __name__ == "__main__":
	print(rotate_array([1, 2, 3, 4, 5], k=2))