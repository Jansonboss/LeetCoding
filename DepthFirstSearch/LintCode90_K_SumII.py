# https://github.com/princeton-nlp/SimCSE

def kSumII(A, k, target):
	A = sorted(A)
	subsets = []
	dfs(A, 0, k, target, [], subsets)
	return subsets
	
def dfs(A, index, k, target, subset, subsets):
	if len(subset) == k and target == 0:
		subsets.append(list(subset))
		return
	
	if k == 0 or target <= 0:
		return
	
	for i in range(index, len(A)):
		subset.append(A[i])
		dfs(A, i + 1, k , target - A[i], subset, subsets)
		subset.pop()

# This is the same thing using k to track
#   def dfs(self, A, index, k, target, subset, subsets):
#         if k == 0 and target == 0:
#             subsets.append(list(subset))
#             return
        
#         if k == 0 or target <= 0:
#             return
        
#         for i in range(index, len(A)):
#             subset.append(A[i])
#             self.dfs(A, i + 1, k - 1, target - A[i], subset, subsets)
#             subset.pop()
if __name__ == '__main__':
	print(kSumII([1,2,3,4], k=2, target=5))