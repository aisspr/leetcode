#Problem 1

"""
Given an array of integers arr, find the maximum sum of a subarray that contains at least one positive number. If no such subarray exists, return 0.
A subarray is a contiguous sequence of elements within an array."""
def maxSubarraySumWithPositive(arr):
    max_sum = 0
    current_sum = 0
    has_positive = False


    if not arr:
        return 0
    
    left, right = 0, len(arr)-1

    for el in arr:
        if el > 0:
            has_positive = True
        current_sum += el
        if current_sum < 0:
            current_sum = 0
        max_sum = max(current_sum, max_sum)
    if has_positive:
        return max_sum
    else:
        return 0



"""You are given a string s containing only lowercase English letters. Your task is to find the length of the longest substring where no character appears more than k times."""

def longestSubstringReatingChar(s, k):
    from collections import defaultdict

    c_cnt = defaultdict(int)
    max_length = 0
    left = 0
    current_l = 0

    for right in range(len(s)):
        right_c = s[right]
        c_cnt[right_c] += 1

        while c_cnt[right_c] > k:
            left_c = s[left]
            c_cnt[left_c] -= 1
            left += 1
        current_l = right - left + 1
        max_length = max(current_l, max_length)
    return max_length


"""You are given a binary tree where each node contains an integer value. Find the maximum sum of any path in the tree. 
A path is defined as any sequence of nodes from some starting node to any ending node along parent-child connections. The path must contain at least one node.
Note: The path does not need to pass through the root and can start and end at any nodes.
"""
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def longestPath(tree):
    max_diam = [0]

    def dfs(node):
        if not node:
            return 0
        left_dept = dfs(node.left)
        right_depth = dfs(node.right)

        diam_at_node = left_dept + right_depth

        max_diam[0] = max(max_diam[0], diam_at_node)
        return max(left_dept, right_depth) + 1
    dfs(tree)
    return max_diam[0]

"""You are planning a road trip and have n cities to visit. You have a car that can travel at most maxDistance kilometers on a full tank.
 There are gas stations in some cities, and you start with a full tank.
Given:

distances: array where distances[i] is the distance from city i to city i+1
gasStations: boolean array where gasStations[i] is true if city i has a gas station
maxDistance: maximum distance your car can travel on a full tank

Determine if it's possible to complete the entire road trip. You must visit cities in order from 0 to n-1.
"""

def canCompleteRoadTrip(distances, gasStations, maxDistance):
    if not distances:
        return True
    n = len(distances)
    current_fuel = maxDistance

    for i in range(n):
        if current_fuel < distances[i]:
            return False
        current_fuel -= distances[i]
        if i<n-1 and gasStations[i+1]: # Refuel if there's a gas station and we're not at the last city
            currentFuel = maxDistance
    return True
