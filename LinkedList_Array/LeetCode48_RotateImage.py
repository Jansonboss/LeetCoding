# https://leetcode.com/problems/rotate-image/
# 先对角线折 然后 再中间对折


def rotate_image(matrix):
	if not matrix: return []


def _flip_in_diagnal(matrix):

	n = len(matrix)
	for i in range(n):
		for j in range(i+1, n):
			matrix[i][j], matrix[j][i] = \
			matrix[j][i], matrix[i][j]
	return matrix
			
def _flip_in_middle(matrix):
	n = len(matrix)
	for i in range(n):
		for j in range(n//2): # 需要减半否则会换完后又换回去
			# 注意这边row是不动的，只换row里面的col
			matrix[i][n-j-1], matrix[i][j] = matrix[i][j], matrix[i][n-j-1]
			#j=0:matrix(0, 4-0-1), matrix[0, 0]
			#j=1:matrix[0, 4-1-1], matrix[0, 1]
	return matrix


# This one bleow should be more intuitive to me
def _flip_in_middle_by_row(matrix):
	for i in range(len(matrix)):
		flip_in_row(matrix[i])
	
def flip_in_row(row):

	# [15, 14, 17, 19] => [19, 17, 14, 15]
	#  0   1   2   3  

	# 0 <-> 3 --> n-i-1
	n = len(row)
	for i in range(len(n)//2):
		row[i] = row[n-i-1]


if __name__ == "__main__":
	matrix =  \
	[[5,1,9,11],
		[2,4,8,10],
		[13,3,6,7],
		[15,14,12,16]]

	matrix = _flip_in_diagnal(matrix)
	for row in matrix: print(row)

	print("\n")
	matrix = _flip_in_middle(matrix)
	for row in matrix: print(row)
