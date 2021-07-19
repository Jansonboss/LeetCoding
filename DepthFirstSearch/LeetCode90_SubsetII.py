# 九章算法小视频： subsetII: duplicated number in the nums

def subset(nums):
	# https://www.youtube.com/watch?v=lCvL8htQ1iI&ab_channel=GoodTecher
	# also see the issue Leetcode90_subsetII_video
	# idx: depth_idx 控制深度层数， i：控制每一层的nums[i]
	"""
			|i= 0   1	2 
			----------------
	depth=0	|	1   2   2
			|	  \
	depth=0	|	1   2   2 
			|         \
	depth=0 |	1   2   2  

													[ ]
												/	 
	0st depth						 	[1]
								/ 			   		\   
	1st depth	    i=1:[1, 2] - repeated- 0 2   i=1:[1, 2]
						/	                     This needed to be removed
	2nd depth 	 i=2: [1, 2, 2]     
	      	  This should be kept
	"""
	if not nums: return []

	nums.sort()
	results, subset, startIdx = [], [], 0
	_dfs(nums, results, subset, startIdx)
	return results

def _dfs(nums, results, subset, idx):
	results.append(subset[:])
	for i in range(idx, len(nums)):
		# for example [1, 2', 2'']
		# duplicated cases're when we finished picking 
		# [1, 2'] (1 is the prefix) and then go to [1, 2'']
		# so the idea is that if we already piclk the 2' then
		# we can ignore the later 2'' => (nums[i-1] == nums[i])
		# so we need to sort first since same number will be put together

		# and there's another case we need to pay attension since idx<= i < endidx
		# when i >= idx: [1, 2', 2''] as normally the program will pick [1, 2']
		# and then go to [1, 2''] this is the duplicated case
		# for example we should keep [1, 2, 2] this is when depth_idx=2=i
		if (i!=0) and (nums[i-1] == nums[i]) and (i > idx):
			continue

		subset.append(nums[i])
		_dfs(nums, results, subset, i+1)
		subset.pop()


if __name__ == '__main__':
	print(subset(nums = [1,2,2]))
	print(subset(nums = [1,1]))