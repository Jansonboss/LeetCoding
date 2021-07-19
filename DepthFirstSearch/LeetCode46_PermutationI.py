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
		# we can also use 
		# since python pass by reference
		# we need copy the subset
		results.append(subset[:]) 
		return

	# think it as a graph, traverse its neighbor
	# the reason why we need visited array in permutations
	# is that we every time we call the _dfs() funciton, 
	# we search from the idx 0 so there might be some values
	# is being visited

	# for combination and subset we don't need visited array since we use
	# idx and i to make sure they don't have the same value 
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