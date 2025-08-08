def find_anagrams(strs):
    result = []
    from collections import defaultdict
    
    anagram_map = defaultdict(list)
    for s in strs:
        canon = ''.join(sorted(s))
        anagram_map[canon].append(s)
    result = []
    for anagram_lst in anagram_map.values():
        anagram_lst.sort()
        result.append(anagram_lst)
    result.sort(key=lambda x:x[0])
    return result

"""You are given an array of n integers and a number k. Your task is to calculate the number of distinct pairs in the array that have a difference of k. 
A pair consists of two integers that are different, and the absolute difference between the integers is exactly k.
The solution is expected to have linear time complexity, i.e., O(n).
"""   
def count_pairs_with_diff_k(nums, k):
    from collections import Counter
    if k < 0:
        return 0
    from collections import Counter
    freq = Counter(nums)
    
    count = 0
    
    if k == 0:
    
        for num_count in freq.values():
            if num_count > 1:
                count += num_count * (num_count - 1) // 2
    else:
        # For each number, count pairs with number + k
        for num in freq:
            if num + k in freq:
                count += freq[num] * freq[num + k]
    
    return count

"""You are given an array of n integers where some integers are repeated. Write a function in Python that takes this array and an integer k as inputs. 
The function needs to return the k most frequent elements from the array in descending order of their frequency. If two numbers have the same frequency, return them in the ascending order. """
def solution(nums, k):
    from collections import Counter
    import heapq
    if k == 0:
        return []
    freq_map = Counter(nums)
    min_heap = []
    
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, -num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
            
    result = []
    
    while min_heap:
        f, n = heapq.heappop(min_heap)
        result.append(-n)
    result.reverse()
    return result