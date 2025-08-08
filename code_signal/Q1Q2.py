def first_duplicate(a):
    seen = set()
    for el in a:
        if el in seen:
            return el
        seen.add(el)
    return -1

#print(first_duplicate([2, 1, 3, 5, 3, 2]))

def adjacent_elements_product(arr):
    max_product = arr[0]*arr[1]
    for i in range(1, len(arr)-1):
        product = arr[i]*arr[i+1]
        max_product = max(product, max_product)
    return max_product

#print(adjacent_elements_product([3, 6, -2, -5, 7, 3]))  # 21

def company_bot_strategy(arr):
    return 1 if arr.count(1) >= arr.count(0) else 0

#print(company_bot_strategy([1, 1, 0, 1, 1]))  # 1
