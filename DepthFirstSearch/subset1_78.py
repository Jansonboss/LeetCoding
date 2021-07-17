def subsets(nums):
	# subsets1: all unique value in the nums
	# https://leetcode.com/problems/subsets/
	if not nums: return []

	nums.sort()
	results, subset, startIdx = [], [], 0
	visited = [0] * len(nums)
	_dfs(nums, startIdx, results, subset, visited)
	return results

def _dfs(nums, idx, results, subset, visited):
	results.append(subset[:])

	for i in range(idx, len(nums)):
		subset.append(nums[i])
		_dfs(nums, i+1, results, subset, visited)
		subset.pop()
	
print(subsets([1, 2, 3]))
print(subsets([3, 2, 1]))