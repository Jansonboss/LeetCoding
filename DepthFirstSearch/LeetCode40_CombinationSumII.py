
def combinationSum2(nums, target):
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
		# if i != 0 and nums[i-1] == nums[i]:
			# continue
		# if nums[i] in subset:
			# continue

		subset.append(nums[i])
		_dfs(nums, results, subset, i+1, target-nums[i])
		subset.pop()
	

if __name__ == "__main__":
	print(combinationSum2(nums=[10,1,2,7,6,1,5], target = 8), "\n")
	print(combinationSum2(nums = [2, 5, 2, 1,2], target = 5), "\n")
	print(combinationSum2(nums=[2, 3, 5], target=8))