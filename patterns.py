#Neighbor Comparison

def compare_with_neighbors(arr):
    """Compare each element with its adjacent elements
        Find local peaks/valleys in data
        Detect anomalies in sequences
        Stock price analysis (higher/lower than previous day)
        Signal processing (detect spikes)
    """
    result = []
    
    for i in range(len(arr)):
        left = arr[i-1] if i > 0 else None
        right = arr[i+1] if i < len(arr)-1 else None
        
        # Various comparison logic
        if left and right:
            if arr[i] > left and arr[i] > right:  # Local peak
                result.append(i)
        elif left:  # Right boundary
            if arr[i] > left:
                result.append(i)
        elif right:  # Left boundary  
            if arr[i] > right:
                result.append(i)
    
    return result

# Sliding window basics
# Find maximum/minimum in subarrays
# Substring problems with constraints
# Stock trading (best time to buy/sell in window)
# Network packet analysis

def fixed_window_max(arr, k):
    """Find maximum in every window of size k"""
    if not arr or k <= 0:
        return []
    
    result = []
    # Process first window
    window_max = max(arr[:k])
    result.append(window_max)
    
    # Slide window
    for i in range(k, len(arr)):
        # Remove element going out of window, add new element
        # Recalculate max for simplicity (can optimize with deque)
        window_max = max(arr[i-k+1:i+1])
        result.append(window_max)
    
    return result

def expanding_window_sum_target(arr, target):
    """Find subarray with sum equal to target"""
    left = 0
    current_sum = 0
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        # Shrink window if sum exceeds target
        while current_sum > target and left <= right:
            current_sum -= arr[left]
            left += 1
        
        if current_sum == target:
            return [left, right]
    
    return [-1, -1]

#Parity patterns

# Data validation (alternating patterns)
# Game logic (alternating player moves)
# Scheduling problems (alternate shifts)
# Binary pattern analysis

def alternating_parity_check(arr):
    """Check if array alternates between even and odd"""
    if len(arr) < 2:
        return True
    
    for i in range(1, len(arr)):
        # Check if current and previous have same parity (both even or both odd)
        if (arr[i] % 2) == (arr[i-1] % 2):
            return False
    return True

def find_alternating_subarrays(arr, k):
    """Find all subarrays of length k with alternating parity"""
    result = []
    
    for i in range(len(arr) - k + 1):
        subarray = arr[i:i+k]
        if alternating_parity_check(subarray):
            result.append([i, i+k-1])  # Return indices
    
    return result

def count_even_odd_pairs(arr):
    """Count pairs where one is even, one is odd"""
    even_count = sum(1 for x in arr if x % 2 == 0)
    odd_count = len(arr) - even_count
    return even_count * odd_count