# https://leetcode.com/problems/permutations/

def permutate1(nums):
	if not nums: return []

	nums.sort()
	results, subset, startIdx = [], [], 0
	visited = [0] * len(nums)
	_dfs(nums, startIdx, results, subset, visited)
	return results

def _dfs(nums, idx, results, subset, visited):

	
	if idx == len(nums): # stop recursion 
		# since python pass by reference
		# we need copy the subset
		results.append(subset[:]) 
		return

	# think it as a graph, traverse its neighbor
	for i in range(0,len(nums)):
		if (visited[i]):
			continue

		subset.append(nums[i])
		visited[i] = 1
		_dfs(nums, idx+1, results, subset, visited)
		# backtracking 
		subset.pop()
		visited[i] = 0
	

if __name__ == "__main__":
	print(permutate1([3, 2, 1]))