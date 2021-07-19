from typing import SupportsBytes


def combinnationSum(nums, target):
	# for combination type of problem
	# use idx, and i tp controll the loop
	# and controll the duplicated or not
	# don't use visited array to do that
	if (not nums) or (not target): return []
	
	# nums = sorted(set(nums))
	results, subset, startIdx = [], [], 0
	_dfs(nums, results, target, startIdx, subset)
	return results

def _dfs(nums, results, target, idx, subset):

	if target == 0:
		results.append(subset[:])
		return
	
	if target < 0:
		return

	for i in range(idx, len(nums)):

		# avoid duplicated if we're not allowed to use set int he beginning
		#  [2, 2, 2, 3]
		#      ^ 
		# if value_i = value_i-1: ignore it
		if nums[i] == nums[i-1] and i > 1:
			continue

		subset.append(nums[i])
		_dfs(nums, results, target-nums[i], i, subset)
		subset.pop()

if __name__ == '__main__':
	print(combinnationSum(nums=[1, 2, 3], target=7), "\n")
	print(combinnationSum(nums=[2, 3, 5], target=8))