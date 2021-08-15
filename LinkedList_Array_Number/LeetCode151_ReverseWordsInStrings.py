# https://leetcode.com/problems/reverse-words-in-a-string/




def ReverseWordString(mystring):

	if not mystrings: return None

	return " ".join(reversed(mystring.split()))