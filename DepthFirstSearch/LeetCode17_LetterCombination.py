# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Using depth first search 但这题有点不同但是虽然我们每个depth要从头开始， 我们用的
# 是idex来控制深度 控制是digits eg. 2 -> 3 -> 4

def LetterCombination(digits):
	"""
		KEYBOARD = {
		2: "a b c",
			|
		3: "d e f",  => this is implicit graph
			|\ 
		4: "g h i", 

		5: "j k i",
		6: "m n o",
		7: "p q r s",
		8: "t u v",
		9: "w x y z"
	}	
	"""
	KEYBOARD = {
		"2": "abc",
		"3": "def",
		"4": "ghi",
		"5": "jki",
		"6": "mno",
		"7": "pqrs",
		"8": "tuv",
		"9": "wxyz"
	}

	if not digits: return []

	results, subset, depth_startIdx = [], [], 0
	_dfs(digits, results, subset, depth_startIdx, KEYBOARD)
	return results

def _dfs(digits, results, subset, depth_startIdx, keyboard):
	# '234' => 
	if len(subset) == len(digits):
		results.append("".join(subset[:]))
		return
	
	for letter in keyboard[digits[depth_startIdx]]:
		subset.append(letter)
		_dfs(digits, results, subset, depth_startIdx+1, keyboard)
		subset.pop()
	
if __name__ == "__main__":
	print(LetterCombination("23"), "\n")
	print(LetterCombination("234"))
