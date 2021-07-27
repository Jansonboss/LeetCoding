# https://www.youtube.com/watch?v=Ber2pi2C0j0&ab_channel=NeetCode

def searchInMatrix(matrix, target):

	height_botom, height_top = 0, len(matrix) - 1

	while height_botom < height_top:

		mid_row = (height_botom + height_top) // 2	

		if target < matrix[mid_row][-1]:
			height_botom = mid_row
		
		elif target > matrix[mid_row][-1]:
			height_top = mid_row

		else:




if __name__ == "__main__":
	matrix = \
	[
		[1, 3, 5, 7],
		[10,11,16,20], # <----
		[23,30,34,60]
	]
	target = 3