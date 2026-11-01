# 347 - Top K Frequent Elements (medium)
# Topics:

# Given an int array nums, and an integer k
#  return the k most frequent elements

# space complexity O(n + m)
# time complexity O(n log(n))


def a(nums, k):
    m = {}
    for val in nums:
        if m.get(val) is None:
            m[val] = 1
        else:
            m[val] = m[val] + 1
    s = sorted(m.items(), key=lambda x: x[1], reverse=True)
    r_ls = [0] * k
    j = 0
    for key in s[:k]:
        r_ls[j] = key[0]
        j += 1
    return s


print(a([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2))
