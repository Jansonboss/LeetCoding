# https://leetcode.com/problems/valid-anagram/
# we can sort the s and t to make compare O(n) = n*nlogn => nlogn
# using hash map O(n) => O(n) since n * O(1)
# similar question: group the anagram
def isAnagram(s, t):
	"""
	:type s: str
	:type t: str
	:rtype: bool
	"""
	if not s or not t: return ""
	if len(s) != len(t):
		return False
	
	s_set, t_set = {}, {}
	for i in range(len(s)):
		s_set[s[i]] = s_set.get(s[i], 0) + 1
		t_set[t[i]] = t_set.get(t[i], 0) + 1
	
	for k in s_set:
		# key k might not inside the t_set
		if s_set[k] != t_set.get(k, 0):
			return False
	return True