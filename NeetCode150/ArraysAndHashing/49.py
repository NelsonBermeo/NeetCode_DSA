# 49 - Group Anagrams (medium)
# Topics - Array, Hashing, String, Sorting

# Given an array of strings strs, group the anagrams together

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Solution 1 - Sorting
# We can create a hashmap where each key is the sorted version of a string and the value is a list of strings
# We iterate through each string in the input list and append the original string to the list corresponding to the key
# Then we add every value into a list and return
# Complexity - O(m * nlog(n)) because we have to sort every string
# Space ...

# Solution 2 - Hash Table with 26 len list
# Instead of sorting each string, we can represent every string by the frequency of its characters. Since the problem uses lowercase English a fixed array of 26 can capture how many times each char appears. Two string are anagrams if their frequency arrays match


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())
