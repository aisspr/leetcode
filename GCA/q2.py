"""Given an array a that contains only numbers in the range from 1 to a.length,
 find the first duplicate number for which the second occurrence has the minimal index. 
 If there are no such elements, return -1.
"""

def firstDuplicate(arr):
    seen = set()
    for el in arr:
        if el in seen:
            return el
        seen.add(el)
    return -1

"""
Given a string s consisting of small English letters, find and return the first 
instance of a non-repeating character in it. If there is no such character, return '_'."""

def firstNotRepeatingCharacter(s):
    cnt = Counter(s)
    for c in s:
        if cnt[c] == 1:
            return c
    return '_'
    
"""You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise)."""

def rotateImage(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    for i in range(n):
        matrix[i].reverse()
    return matrix

"""valid sudoku"""

def sudoku2(gird):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            el = grid[i][j]

            if '.' in el:
                continue
            if el in rows[i]:
                return False
            rows[i].add(el)

            if el in cols[j]:
                return False
            cols[j].add(el)

            box_idx = (i//3)*3 + (j//3)
            if el in boxes[box_idx]:
                return False
            boxes[box_idx].add(el)
    return True


"""
You are given a list of dishes, where each dish is represented by a list of its ingredients. 
You want to group the dishes by ingredients, so that for each ingredient you'll be able to find all the dishes that contain it.
Return a list where each element is a list which first element is the name of the ingredient and all the other elements are 
the names of dishes that contain this ingredient. The dishes inside each group should be sorted lexicographically, and the groups 
themselves should be sorted lexicographically by the ingredient name."""

def groupingDishes(dishes):
    ingredient_map = {}
    for dish in dishes:
        dish_name = dish[0]
        for ingredient in dish[1:]:
            if ingredient not in ingredient_map:
                ingredient_map[ingredient] = []
            ingredient_map[ingredient].add(dish_name)
    
    result = []
    for ingredient in sorted(ingredient_map):
        result.append([ingredient]+sorted(ingredient_map[ingredient]))
    return result



"""
Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k."""
def __init__(self, x):#     
	self.val = x     
	self.next = None

def removeKfromList(l, k):
    if not l:
        return l
    
    while l and l.val == k:
        l = l.next

    current = l
    while current and current.next:
        if current.val == k:
            current.next = current.next.next
        else:
            current = current.next # equivalent of +=1
    return l 

"""
Given a sorted integer array that does not contain any duplicates, return a summary of its ranges."""

def composeranges(nums):
    if not nums:
        return []
    
    start = nums[0]
    end = nums[0]
    result = []

    for i in range(1, len(nums)):
        if nums[i] == end+1:
            end = nums[i]
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}->{end}")
            start = end = nums[i]

    if start == end:
        result.append(str(start))
    else:
        result.append(f"{start}->{end}")

    return result

"""
You have a collection of coins, and you know the values of the coins and the quantity of each type of coin in it.
 You want to know how many distinct sums you can make from non-empty groupings of these coins."""

def possibleSums(coins, quantity):
    possible = {}

    for i in range(len(coins)):
        all_coins = []
        for coin, cnt in zip(coin, quantity):
            all_coins.extend([coin]*cnt)

        possible = {0}
        for coin in all_coins:
            possible = possible or {summ+coin for summ in possible}
    return len(possible) -1

"""
You are given a string code that contains only '0's and '1's, along with a binary code. 
Your task is to decode this binary code into readable text."""

def messageFromBinaryCode(code):
    result = ""
    for i in range(0, len(code, )):
        byte = code[i:i+8]
        result += chr(int(byte, 2))
    return result 

"""Apply box blur filter to the image represented as an integer matrix."""

def boxBlur(image):
    rows, cols = len(image), len(image[0])

    blurred_image = []

    for i in range(1, rows-1):
        row = []
        for j in range(1, cols-1):
            total_sum = 0
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    total_sum += image[x][y]
            average = int(total_sum/9)
            row.append(average)
        blurred_image.append(row)
    return blurred_image


"""In the popular Minesweeper game you have a board with some mines and those cells
 that don’t contain a mine have a number in it that indicates the total number of mines in the 
 neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup."""

def minesweeper(matrix):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0,1), (0,-1), (-1,0), (1,0)]

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            cnt = 0
            for dr, dc in directions:
                nr, nc = i+dr, j+dc
                if 0 <= i < rows and 0 <= j < cols and matrix[nr][nc]:
                    cnt += 1
            row.append(cnt)
        result.append(row)
    return result
            

"""
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem."""

def arrayReplace(arr, elemToReplace, substitutionElem):
    return [substitutionElem if el==elemToReplace else el for el in range(len(arr))]

"""Check if all digits of the given integer are even.
"""

def evenDigitsOnly(n):
    return all(int(digit) % 2 == 0 for digit in str(n))

"""Define a word as a sequence of consecutive English letters. Find the longest word from the given string.
"""

def longestWord(text):
    for c in text:
        if not c.isalpha():
            text = text.replace(c, ' ')

    words = text.split()
    return max(words, key=len) if words else ''

"""Given an array of integers, find the maximal absolute difference between any two adjacent elements."""
def arrayMaximalAdjacentDifference(arr):
    diff = []
    for i in range(1, len(arr)-1):
        d = abs(arr[i-1]-arr[i])
        diff.append(d)
    return max(diff)

"""An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a
 computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, 
 and thus two versions of addresses. Today we'll be dealing with IPv4."""

def isValidIP4(address):
    split = address.split('.')
    if len(split) != 4:
        return False

    for el in split:
        if not el or len(el) > 3:
            return False
        if not el.isdigit():
            return False
        elif not 0 <= int(el) <= 255:
            return False
        elif el[0] == '0' and len(el) > 1:
            return False
    return True


"""You are given an array of integers representing coordinates of obstacles situated on a straight line. 
Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps 
of the same length represented by some integer. Find the minimal length of the jump enough to avoid all obstacles."""

def avoidObstacles(arr):
    obstacles = set(arr)
    jump_length = 1

    while True:
        is_safe = True
        for obstacle in arr:
            if obstacle % jump_length == 0:
                is_safe = False
                break
        if is_safe:
            return jump_length
        jump_length += 1


"""Given an integer, find its digit degree - 
the number of times you have to replace it with the sum of its digits until you get to a single digit number.
"""

def digitalDegree(n):
    cnt = 0
    while n>=10:
        n = sum(int(digit) for digit in str(n))
        cnt += 1
    return cnt

"""
Each day a plant is growing by upSpeed meters. Each night that plant's height decreases by downSpeed meters due 
to the lack of sun heat. Initially, plant is 0 meters tall. We plant the seed at the beginning of a day. We want 
to know when the height of the plant will reach a certain level."""

def growingPlant(upSpeed, downSpeed, desiredHeight):
    if upSpeed >= desiredHeight:
        return 1
    days = 0
    height = 0

    while height < desiredHeight:
        days += 1
        height += upSpeed 
        if height >= desiredHeight:
            break
        height -= downSpeed
    return days

"""You found two items in a treasure chest! The first item weighs weight1 and is worth value1, 
and the second item weighs weight2 and is worth value2. You have a knapsack that can hold at most maxW weight units.
 Which items should you take to maximize the total value? (Return the maximum value.)
"""

def knapsackLight(value1, weight1, value2, weight2, maxW):
    maxValue = 0

    maxValue = max(maxValue, 0) #take nothing

    if weight1 <= maxW: #take only 1
        maxValue = max(maxValue, value1)
    
    if weight2 <= maxW: #take only 2
        maxValue = max(maxValue, value2)

    if weight1+weight2 <= maxW: #take both
        maxValue = max(maxValue, value1+value2)

    return maxValue

"""
Given a string, output its longest prefix which contains only digits."""

def longestDigitsPrefix(input):
    result = ''
    for c in input:
        if c.isdigit():
            result += c
        else:
            break
    return result
        
"""
Given integers a and b, determine whether the following statement is true or 
false: The sum of the digits of a*b is equal to the sum of the digits of a multiplied by the sum of the digits of b.
"""

def digitSumMatching(a,b):
    sum_prod = sum(int(d) for d in str(a*b))
    sum_second = sum(int(d) for d in str(a)) * sum(int(d) for d in str(b))
    return sum_prod == sum_second

"""Check if the given string is a valid time representation of a 24-hour clock.
"""
def validTime(input):
    if len(input) != 5 or input[2] != ':':
        return False
    try:
        hours = input[:2]
        min = input[3:]

        if 0 <= hours <= 23 and 0 <= min <= 59:
            return True
    except:
        return False

"""The core goal is to extract all the numbers from a given string and calculate their total sum.
"""
def sumUpNumbers(input):
    import re
    numbers = re.findall(r'\d+', input)
    return sum(int(el) for el in numbers)

"""Given a rectangular matrix containing only digits, calculate the number of different 2×2 squares in it.
"""

def differentSquares(matrix):
    rows, cols = len(matrix), len(matrix[0])
    if len(rows) < 2 or len(cols) < 2:
        return 0
    
    squares = set()

    for i in range(rows-1):
        for j in range(cols-1):
            square = (matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1])
            squares.add(square)
    return len(squares)

"""Given an integer product, find the smallest positive integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.
"""
def digitsProduct(product):
    if product == 0:
        return 10
    if product == 1:
        return 1
    
    digits = []

    for d in range(9, 1, -1):
        while product % d == 0:
            digits.append(d)
            product //= d
    
    if product > 1:
        return -1
    
    return int(''.join(map(str, sorted(digits))))

"""
You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later 
will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.
"""   
def fileNaming(names):
    seen = set()
    result = []

    for n in names:
        if n not in seen:
            seen.add(n)
            result.append(n)
        else:
            k = 1
            while n+'('+str(k)+')' in seen:
                k += 1
            new_n = n+'('+str(k)+')'
            seen.add(new_n)
            result.append(n)
    return result

"""Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
"""
def repeatedSubstring(input)
    return input in (input+input)[1:-1]

"""
"""
def isPrime(n):
    if n < 2:
        return False
    if n== 2:
        return True
    if n%2 ==0:
        return False
    for i in range(3, int(n**0.5), 2):
        if n % i == 0:
            return False
    return True


"""Find the greatest common divisor of two integers.
"""
def gdc(a, b):
    while b:
        a, b = b, a%b
        return a
    
"""Given two integers representing the numerator and denominator of a fraction, return the fraction in string format. 
If the fractional part is repeating, enclose the repeating part in parentheses.
"""
            
def fraction2Decimal(num, den):
    if num == 0:
        return 0
    result = ''

    if (num<0) != (den<0):
        result += '-'
    num, den = abs(num), abs(den)

    #integer part
    result += str(num // den)

    #fraction
    remainder = num % den
    if remainder == 0:
        return result
    result+= '.'

    remainder_map = {}

    while remainder != 0:
        if remainder in remainder_map:
            index_start = remainder_map[remainder]
            result = result[:index_start] + '(' + result[:index_start:] + ')'
            return result
        remainder_map[remainder] = len(result)
        next_digit = remainder // den
        result += str(next_digit)
        remainder %= den
    return result

            
"""Given an array of integers where each integer >= 0, apply the following steps repeatedly until all numbers are 0, then return the accumulated answer:

1. Find the first non-zero element in the array starting from the left. Call this value `x`.
2. Starting at your current location, subtract `x` from each number until you reach a number that is less than `x`.
3. Add `x` to your answer.
4. Repeat from step 1.
"""

def arrayReduction(arr):
    ans = 0
    i = 0
    while i < len(arr):
        while i < len(arr) and arr[i] == 0:
            i+= 1
        if i >= len(arr):
            break
        x=arr[i]
        ans += x
        while i<len(arr) and arr[i] >= x:
            arr[i] -= x
            i+=1
    return ans
















