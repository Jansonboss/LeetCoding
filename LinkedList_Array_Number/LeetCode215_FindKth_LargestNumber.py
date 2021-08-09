# https://leetcode.com/problems/kth-largest-element-in-an-array/
# https://www.jiuzhang.com/problem/kth-largest-element/
# https://github.com/Jansonboss/LeetCoding_Practice/blob/main/Others/MyCollecions_QuickSort.py

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# this question could be same to find median

# we can use Quckselect to find the Kth largest in unsorted array -> O(n)
# if do sort and then find Kth largest then O(nlogn)


# [23, 34, 5, 1, 34, 54, 3]
# [ 1, 5, 3, 23, 53, 34, 34]
#             |       |
#          pivot_idx    


# T(n) = T(n/2) + O(n) = T(n/4) + O(n/2) + O(n) ... = O(2n)


# Quick Select

def Find_Kth(nums, k): 

	if not nums or not k: return None
	start, end = 0, len(nums) - 1
	k = len(nums) - k

	result = _partition(nums, start, end, k)
	return result

def _partition(nums, start, end, k):

	if start == end: return nums[k]

	pivot = start
	while start <= end:
		while nums[start] < nums[pivot]:
			start += 1
		while nums[end] > nums[pivot]:
			end -= 1	
		if start > end:
			break
		nums[start], nums[end] = nums[end], nums[start]
		start, end = start + 1, end - 1

	# now the right < left
	if k > left:
		_partition(nums, start = left, end = end , k)
	if k < right:
		_partition(nums, start = start, end = right , k)
	return nums[k]









# Piroity Queue (also good for K largest stream)