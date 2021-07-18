from typing import SupportsBytes


def combinnationSum(nums, target):
	# for combination type of problem
	# use idx, and i tp controll the loop
	# and controll the duplicated or not
	# don't use visited array to do that
	if (not nums) or (not target): return []

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
		subset.append(nums[i])
		_dfs(nums, results, target-nums[i], i, subset)
		subset.pop()

if __name__ == '__main__':
	print(combinnationSum(nums=[1, 2, 3], target=7), "\n")
	print(combinnationSum(nums=[2, 3, 5], target=8))