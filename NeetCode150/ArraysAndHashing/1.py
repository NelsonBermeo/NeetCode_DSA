# 1 - Two Sum (easy)
# Topics - Array, Hashing

# You are given an array of integers nums and a int target, return the indices of the two numbers such that they add up to target

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# I don't think sorting is a solution here

# Solution 1: Brute Force
# We can double loop through the list and see if we have 2 indices that are not the same with a if check that add up to target
# Time - O(n^2)
# Space - O(1) not using any other structures

# Solution 2: HashMap
# We'd create a map of [target - nums[i]] = index
# We would loop through the original list again and check if the value at the index even exists in the map. If it does that mean we have a pair. We also check if the value of that map component is not the current index because then we'd be adding with outselves. We'd then return the current index int he loop and the value of hashmap[value]
# Time - O(n) since we just loop
# Space - O(n) since we have to make a set


def a(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        hashmap[target - nums[i]] = i
    for j in range(len(nums)):
        if hashmap[nums[j]] is not None and hashmap[nums[j]] != j:
            return [hashmap[nums[j]], j]


print(a([2, 7, 11, 15], 9))
