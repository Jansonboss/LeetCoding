# original link: https://leetcode.com/problems/palindrome-partitioning/

# 所有的切割问题都是combination probelm (dfs) see below:
# https://github.com/Jansonboss/LeetCoding/blob/main/DepthFirstSearch/LeetCode90_SubsetII.py

# dfs question eg. (all paths, partitions, all the solutions, cheese board...) 
# aab -> 0a1a2b ([0, 1, 2]: combination problem 先切在2和后切在2是一样的order does not matter)
# on the other hand上一刀切在哪儿下一刀是要从上一刀的下一个位置开始切 （combination）use idx to controll
# a = "a a a b" => a[:2]: aa => a[:1]: a
#       ^ ^

from typing import SupportsBytes


def partition(s):

	if not s: return [""]

	results, subset, start_depth_idx = [], [], 0
	_dfs(s, results, subset, start_depth_idx)
	return results

def isPalin(substring):
	# TODO this place could be optimzied with DP
	return substring[:] == substring[::-1]

def _dfs(s, results, subset, depth_start_idx):
	
	if depth_start_idx == len(s):
		# depth of the recursion tree is the length of s
		results.append(subset[:])
		return 
	
	for i in range(depth_start_idx, len(s)):
		# 边切边check
		substring = s[depth_start_idx:i+1]
		if not isPalin(substring):
			continue
		
		subset.append(substring)
		_dfs(s, results, subset, i+1)
		subset.pop()


if __name__ == "__main__":
	print(partition(s="aab"), "\n")
	print(partition(s="aabaa"), "\n")