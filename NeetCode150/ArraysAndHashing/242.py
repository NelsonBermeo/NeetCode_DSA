# 242 - Valid Anagram (easy)
# Topics - Hashing, String, Sorting

# Given two strings s and t return true if t is an anagram of s and false otherwise. I believe an anagram is another word that can be made with the same chars as another

# s = "anagram", t = "ngaram" -> false

# You couldn't really double loop for this because you could count a char twice in the 2nd string by accident

# Solution 1: Sorting & Comparing
# We could sort each string and then loop through them and see if they are the same
# Time - O(nlog(n)) because sorting
# Space - O(1) unless sorting uses a linear data structure

# Solution 2: HashMap
# We could loop through each word and make a seperate hashmap for each and compare the hashmaps.
# Time - O(n) because we have to loop through the strings
# Space - O(n) because we have those maps in storage now


def a(s, t):
    s_map = {}
    t_map = {}
    for i in s:
        if s_map.get(i) == None:
            s_map[i] = 1
        else:
            s_map[i] += 1
    for i in t:
        if t_map.get(i) == None:
            t_map[i] = 1
        else:
            t_map[i] += 1
    if t_map == s_map:
        return True
    return False


print(a("anagram", "ngaram"))
