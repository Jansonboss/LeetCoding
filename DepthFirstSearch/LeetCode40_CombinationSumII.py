
#	https://leetcode.com/problems/combination-sum-ii/
#	Given a collection of candidate numbers (candidates) and a target number (target),

#	find all unique combinations in candidates where the candidate numbers sum to target.
#	Each number in candidates may only be used once in the combination.

#	Note: The solution set must not contain duplicate combinations.

def combinationSum2(nums, target):
	# this is excatly the same staff with subsetII https://leetcode.com/problems/subsets-ii/
	# https://github.com/Jansonboss/LeetCoding/blob/main/DepthFirstSearch/LeetCode90_SubsetII.py
	# we need to remove the duplicated ele
	# 【1， 2‘， 2’‘】
	#   0   1   2 
	# 只要我发现他跳过了 【1， 2’】 去选择了【1， 2‘’】我就continue
	# 如果他选择了【1， 2‘】 然后又加了2’‘ -》 【1， 2’， 2‘’】 这是可以的
	if not nums or not target: return []

	nums = sorted(nums)

	results, subset, startIdx = [], [], 0
	_dfs(nums, results, subset, startIdx, target)
	return results

def _dfs(nums, results, subset, idx, target):
	
	if target == 0:
		results.append(subset[:])
	
	if target < 0:
		return

	for i in range(idx, len(nums)):
		if (i > idx) and (nums[i-1] == nums[i]):
			continue
		subset.append(nums[i])
		_dfs(nums, results, subset, i+1, target-nums[i])
		subset.pop()
	

if __name__ == "__main__":
	print(combinationSum2(nums=[10,1,2,7,6,1,5], target = 8), "\n")
	print(combinationSum2(nums = [2, 5, 2, 1,2], target = 5), "\n")
	print(combinationSum2(nums=[2, 3, 5], target=8))