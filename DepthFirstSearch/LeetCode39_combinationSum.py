def combinationSum(candidiates, target):
	if not candidiates or not target: return []

	results, subset, startIdx = [], [], 0
	_dfs(candidiates, results, subset, startIdx, target)
	return results

def _dfs(candidates, results, subset, idx, target):
	pass
