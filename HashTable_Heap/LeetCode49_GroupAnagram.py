# https://www.youtube.com/watch?v=vzdNOK2oB2E&ab_channel=NeetCode
# hash map (not prefix since we cannot use prefix for anangram problem)
# unless we sort all the words alphabically

def groupAnagram_hash(strings):
	if not strings: return []

	from collections import defaultdict

	recorder = defaultdict(list)

	for word in strings:
		sorted_word = "".join(sorted(word)) # m * nlogn => number of word in list * time we sort each of them
		recorder[sorted_word].append(word)
	return list(recorder.values())


def groupAnagram_Trie_like(strings):
	if not strings: return []
	
	from collections import defaultdict
	recorder = defaultdict(list)

	for word in strings:
		key = [0] * 26
		for char in word: # create char distribution anagram will have same distribution of char
			key[ord(char) - ord("a")] += 1
		recorder[tuple(key)].append(word) # don't use (key)
	return list(recorder.values())
		







if __name__ == "__main__":
	strs = ["eat","tea","tan","ate","nat","bat"]
	print(groupAnagram_hash(strs), "\n")

	strs = ["a"]
	print(groupAnagram_hash(strs), "\n")
	
	strs = ["eat","tea","tan","ate","nat","bat"]
	print(groupAnagram_Trie_like(strs), "\n")

	strs = ["a"]
	print(groupAnagram_Trie_like(strs), "\n")
	