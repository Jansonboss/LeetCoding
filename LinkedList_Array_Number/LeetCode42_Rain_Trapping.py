# https://leetcode.com/problems/trapping-rain-water/
# min(l, r) - h[i]

# height =   [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# maxleft =  [0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3]
# maxRight = [                              1 , 0]

# min(l,r) = [0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3]

from collections import deque

def trapped_rain(heights):

	if not isinstance(heights, list): return None
	if not heights: return None

	maxLeft, maxRight = [0], deque([0])
	left, right = 0, len(heights) - 1
	maxLeft_sofar, maxRight_sofar = heights[0], heights[-1]

	while left < len(heights) and right > 0:
		maxLeft_sofar, maxRight_sofar = max(maxLeft_sofar, heights[left]), max(maxRight_sofar, heights[right])
		maxLeft.append(maxLeft_sofar)
		maxRight.appendleft(maxRight_sofar)
		left, right = left + 1, right - 1 
	
	min_left_right = [min(l, r) for l, r in zip(maxLeft, maxRight)]
	result = sum([l - r if l - r > 0 else 0 for l, r in zip(min_left_right, heights)])
	return result



if __name__ == "__main__":
	print(trapped_rain(heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))