# Two Pointers and Quick select
# are able to solve Kth largest number


# https://www.jiuzhang.com/problem/kth-largest-element/


# https://www.youtube.com/watch?v=7h1s2SojIRw&t=1s&ab_channel=AbdulBari
# We first pick the 0th item in the list as pivot
# and have i index point to 0th and j index point to len(nums) - 1 position
# [10, 16, 8, 12, 15, 6, 3, 9, 5, inf]
#  |							   |
#  i							   j

# so the idea is that we firstly need to find a pivot
# anything below pivot will be move to left and the one above to the right
# increment i unitl you find ele > 10 and descrease j until find ele < 5
# swap i and jth element in the array until i and j cross
# Pivot value is the jth element (every element on the left side of pivot smaller than pivot)
# and (every element on the right side of pivot bigger than pivot) => pivot is sorted


def _partition(nums, l, r):

	pivot = l
	while True:
		while nums[l] < nums[pivot]:
			l += 1
		while nums[r] > nums[pivot]:
			r -= 1
		if l >= r:
			nums[r], nums[pivot] = nums[pivot], nums[r]
			print("Done", nums)
			return r
		nums[l], nums[r] = nums[r], nums[l]
		print("switch", nums)
		l += 1
		r -= 1
	return pivot


def quickSort(nums, l, r):
	if l > r: return 
	pivot = _partition(nums, l, r)
	quickSort(nums, l = l, r = pivot - 1)
	quickSort(nums, l = pivot + 1, r = r)


def sort(nums):
	l, r = 0, len(nums) - 1
	quickSort(nums, l, r)
	return nums


if __name__ ==  "__main__":
	print(sort(nums = [10, 16, 8, 12, 15, 6, 3, 9, 5]))
	print("\n")
	print(sort(nums = [10, 16, 21, 4, 12, 34, 1, 3]))




