# Problem 1: Alternating Parity Window
def solution(numbers, k):
    """
    Find count of subarrays of length k where elements alternate between even and odd
    """
    count = 0
    for i in range(len(numbers) - k + 1):
        valid = True
        for j in range(i + 1, i + k):
            if numbers[j] % 2 == numbers[j-1] % 2:
                valid = False
                break
        if valid:
            count += 1
    return count

# Problem 2: Local Peaks
def solution(numbers):
    """
    Return array where 1 indicates element is greater than both neighbors
    """
    result = []
    for i in range(len(numbers)):
        is_peak = True
        if i > 0 and numbers[i] <= numbers[i-1]:
            is_peak = False
        if i < len(numbers)-1 and numbers[i] <= numbers[i+1]:
            is_peak = False
        result.append(1 if is_peak else 0)
    return result