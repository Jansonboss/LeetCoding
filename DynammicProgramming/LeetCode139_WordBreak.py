def wordBreak(s, wordDict):

	if (not s) or (not wordDict): return None

	dp = [0] * (len(s) + 1)
	print(dp)
	dp[len(s)] = True
	print(dp)

	for i in range(len(s)-1, -1, -1):
		print(i)
		for w in wordDict:
			print(w, dp)
			if ((i + len(w)) <= len(s)) and (s[i: i+len(w)] == w):
				print(dp[i+len(w)])
				dp[i] = dp[i + len(w)]
				print(dp)
			if dp[i]:
				break
	return dp[0]
		
if __name__ == "__main__":
	print(wordBreak("neetcode", wordDict=["neet", "leet", "code"]))