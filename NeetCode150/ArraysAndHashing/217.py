# 217 - Contains Duplicate (easy)
# Topics: Array, Hashtable, Sorting

# Given nums return true if any value appears at least twice

# Solution 1: Brute Force
# You can brute force with a douple loop and check if an element appears in the rest of the array
# Time - O(n^2)
# Space - O(1)

# Solution 2: Sorting
# You can sort the array with Python's built in sort function and that'd use Timsort or Powersort which has a runtime of O(nlog(n)) then you can compare every element to the one before it and you can easily find a duplicate there.
# Time - O(nlog(n))
# Space - O(n) perhaps if our sort uses a list of some sort.

# Solution 3:
#
