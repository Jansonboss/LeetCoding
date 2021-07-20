
# https://leetcode.com/problems/permutations-ii/
# Input: nums = [1,1,2]
# Output: [ [1,1,2], [1,2,1], [2,1,1] ]
# we don't need depth_startIdx since we need to do permutation and 
# for each depth level, we need to start from index = 0 so we need visited array
# this question is also sam as print all the **Anagram**

# video link: https://github.com/Jansonboss/LeetCoding/issues/3
def permutation2(nums): 

	if not nums: return []

	nums.sort()
	results, subset, depth_startIdx = [], [], 0
	visited = [0] * len(nums)
	_dfs2(nums, results, subset, depth_startIdx, visited)
	return results

def _dfs2(nums, results, subset, depth_startIdx, visited):
	# no need depth_startIdx
	if len(subset) == len(nums):
		results.append(subset[:])
		return

	for i in range(0, len(nums)):
		# pruning
		# if visited[i]: continue
		#            ^
		#            |
		# (if include this, remove everything after or)

		if ((nums[i] == nums[i-1]) and (not visited[i-1])) or (visited[i]):
			continue	

		visited[i] = 1
		subset.append(nums[i])
		_dfs2(nums, results, subset, i+1, visited)
		visited[i] = 0
		subset.pop()


# https://www.jiuzhang.com/solutions/string-permutation-ii

# 给出一个字符串，找到它的所有排列，注意同一个字符串不要打印两次。
# s = "abb" no duplicated
#输出：["abb", "bab", "bba"] =>  this is anagram


def printAnagram(s):
	
	if not s: return []

	s = sorted(s)
	results, subset, depthStartIdx = [], [], 0
	visited = [0] * len(s)
	_dfs(s, results, subset, visited)
	return results


def _dfs(s, results, subset, visited):
    
	if len(subset) == len(s):
		results.append("".join(subset[:]))
	
	for i in range(0, len(s)):
		if visited[i]:
			continue
		
		visited[i] = 1
		subset.append(s[i])
		if (s[i] == s[i-1]):
			continue
		_dfs(s, results, subset, visited)
		visited[i] = 0
		subset.pop()

if __name__ == "__main__":
	print(permutation2(nums=[1, 1, 2]))
	print(printAnagram('leet'))