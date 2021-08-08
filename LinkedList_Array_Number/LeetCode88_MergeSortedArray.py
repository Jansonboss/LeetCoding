# https://leetcode.com/problems/merge-two-sorted-lists/
# A = [1, 6, 8, empty, empty], 
#      |     |
# 
# B = [4, 5]
#      |

def mergeSortedArray(nums1, nums2):
	if (not nums1) or (not nums2):
		return None
	
	last1, last2, end = len(nums1) - 1, len(nums2) - 1, len(nums1) - 1
	
	while last1 >= 0:
		if nums1[last1] == "empty":
			last1 -= 1
		else:
			break
	
	while last1 >= 0 and last2 >= 0:
		
		if nums1[last1] > nums2[last2]:
			nums1[end] = nums1[last1]
			end -= 1
			last1 -= 1
		else:
			nums1[end] = nums2[last2]
			end -= 1
			last2 -= 1
	return nums1


if __name__ == "__main__":
	print(mergeSortedArray(nums1 = [1, 6, 8, "empty", "empty"], nums2 = [4, 5]))
	
	


