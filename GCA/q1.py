#GCA Q1

"""Given a year, return the century it belongs to. 
The first century spans from the year 1 up to and including the year 100, the second from 101 to 200, etc.
"""
def giveCentury(year):
    return (year+99)//100

"""Given a year, return the century it belongs to. 
The first century spans from the year 1 up to and including the year 100, the second from 101 to 200, etc.
"""
def checkPalindrome(word):
    #return word == word[::-1]
    left, right = 0, len(word)-1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

"""Given an array of integers, find the pair of adjacent elements that 
has the largest product and return that product."""

def adjacentElementsProduct(arr):
    max_product = arr[0], arr[1]
    for i in range(1, len(arr)-1):
        product = arr[i-1]*arr[i]
        max_product = max(max_product, product)
    return max_product

def makeArrayConsecutive2(arr):
    if not arr:
        return 0
    return max(arr) - min(arr) + 1 - len(arr)

"""Given a sequence of integers as an array, determine whether it is possible to obtain 
a strictly increasing sequence by removing no more than one element from the array."""

def almostIncreasingSequence(arr):
    cnt = 0
    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]:
            cnt += 1
            if cnt > 1:
                return False
        #check if we can fix by removing current or next element
        if (i>0 and i+1 < len(arr)-1) and (arr[i-1]>=arr[i+1]) and (arr[i]>=arr[i+2]):
            return False
    return True 
            
            
"""
- Sum matrix elements avoiding columns with zeros (ghosts)
    You have a matrix representing rooms in a building
    - Each room has a value (rent/cost)
    - Rooms with value 0 contain ghosts
    - If a room has a ghost, all rooms below it in the same column are also haunted and unusable
    - You need to sum up the values of all usable (non-haunted) rooms
    """       

def matrix_elements_sum(matrix):
    rows, cols = len(matrix), len(matrix[0])
    total = 0
    for col in range(cols):
        for row in range(rows):
            if matrix[row][col] == 0:
                break
            total += matrix[row][col]
    return total
   
#print (matrix_elements_sum([[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]))

def allLongestStrings(arr):
    """
    Given an array of strings, return another array containing all of its longest strings.
    """
    max_len = 0
    for el in arr:
        max_len = max(max_len, len(el))
    
    return [word for word in arr if len(word)== max_len]

def commonCharacterCount():
    """
    Given two strings, find the number of common characters between them.
    """
    def commonCharacterCount(s,t):
        from collections import Counter

        cnt1 = Counter(s)
        cnt2 = Counter(t)

        common = 0
        for c in cnt1:
            if c in cnt2:
                common += min(cnt1[c], cnt2[c])
        return common

    """Ticket numbers usually consist of an even number of digits. A ticket number is considered 
    lucky if the sum of the first half of the digits is equal to the sum of the second half."""
def isLucky(n):
    n = str(n)
    mid = len(n)//2
    return sum(arr[:mid]) == sum(arr[mid:])

"""
Given an integer n, return the largest number that contains exactly n digits and all digits are different.
"""
def largestNumber(n):
    if n > 10:
        return -1
    return int(''.join([str(9-i) for i in range(n)]))

"""
Some people are standing in a row in a park. There are trees between them which cannot be moved. 
Your task is to rearrange the people by their heights in non-descending order without moving the trees."""

def sortByHeight(arr):
    temp = sorted([el for el in arr if el != -1])
    j = 0
    for i in range(len(arr)):
        if arr[i] != -1:
           arr[i] = temp[j]
           j+= 1
    return arr

#print (sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))

"""
Write a function that reverses characters in (possibly nested) parentheses in the input string."""
def reverseInParentheses(input):
    while '(' in input:
        start = input.rfind('(')
        end = input.find(')')

        before = input[:start]
        middle = input[start+1:end][::-1]
        after = input[end+1:]

        input = before + middle + after
    return input


"""
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.
"""
def variableName(name):
    if not name or name[0].isdigit():
        return False
    return all(c.isalnum() or c=='_' for c in name)

"""Given a string, your task is to replace each of its characters by the next one in the English alphabet; 
i.e. replace a with b, replace b with c, etc (z should be replaced by a).
"""
def alphabeticShift(input):
    result = ''
    for c in input:
        if c == 'z':
            result += 'a'
        else:
            result += chr(ord(c)+1)
    return result

"""Given two cells on the standard chess board, determine whether they have the same color or not.
"""
def chessBoardCellColor(cell1, cell2):
    color1 = (ord(cell1[0]) + int(cell1[1])) % 2
    color2 = (ord(cell2[0]) + int(cell2[1])) % 2

    return color1 == color2

"""
Consider integer numbers from 0 to n - 1 written down along the circle in such a way 
that the distance between any two neighboring numbers is equal (note that 0 and n - 1 
are neighboring, too). Given n and firstNumber, find the number which is written 
in the radially opposite position to firstNumber.
"""

def circleOfNumbers(n, first):
    return (first + n // 2) % n

"""
You have deposited a specific amount of money into your bank account. Each year your 
balance increases at the same growth rate. Find out how many years it will take for 
your balance to pass a specific threshold with the assumption that you don't make any additional deposits.
"""

def depositProfit(deposit, rate, threshold):
    years = 0
    current = deposit
    while current < threshold:
        current += current*rate/100
        years += 1
    return years

"""
Given a sorted array of integers a, find an integer x from a such that the value of 
abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x) is the smallest possible.
"""
def absoluteValuesSumMinimization(arr):
    sums = {}
    for el in arr:
        total = sum([abs(arr[i]-el) for i in range(len(arr))])
        if total in sums:
            sums[total] = min(el, sums[total])
        else:
            sums[total] = el
    return sums[min(sums)]

"""
Given an array of equal-length strings, check if it is possible to rearrange the 
strings in such a way that after the rearrangement the strings at any two adjacent 
positions would differ by exactly one character.
"""

def stringsRearrangement(input):
    from itertools import permutations
    def differsByOne(a, b):
        return sum(c1 != c2 for c1, c2 in zip(a,b)) == 1
    
    def isValid(arr):
        for i in range(len(arr)-1):
            if not differsByOne(arr[i], arr[i+1]):
                return False
        return True
    
    for perm in permutations(input):
        if isValid(perm):
            return True
    return False

"""
Given array of integers, remove each kth element from it."""
def extractEachKth(arr, k):
    return [input[i] for i in range(len(arr)) if (i+1)%k != 0]

"""Find the leftmost digit that occurs in a given string."""
def firstDigit(input):
    for c in input:
        if c.isdigit():
            return c
    return ""

"""Given a rectangular matrix of characters, add a border of asterisks(*) to it."""
def addBorder(picture):
    width = len(picture[0]) + 2
    border = '*'*width

    result = [border]

    for row in picture:
        result.append('*'+row + '*')
    result.append(border)

    return result

"""
Two arrays are called similar if one can be obtained from another by swapping at 
most one pair of elements in one of the arrays."""

def areSimilar(a,b):
    diffs = [i for i in range(len(a)) if a[i] != b[i]]
    if len(diffs)== 0:
        return True
    if len(diffs) == 2:
        return a[diffs[0]] == b[diffs[1]] and a[diffs[1]] == b[diffs[0]]
    return False

"""
You are given an array of integers. On each move you are allowed to increase exactly one of 
its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.
"""

def arrayChange(arr):
    moves = 0
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            needed = arr[i-1]+1-arr[i]
            moves += needed
            arr[i] = arr[i-1] +1
    return moves

"""
Given a string, find out if its characters can be rearranged to form a palindrome."""

def palindromeRearranging(input):
    from collections import Counter
    char_cnt = Counter(input)
    odd_cnt = sum(1 for cnt in char_cnt.values() if count %2 == 1)
    return odd_cnt <= 1

"""
Call two arms equally strong if the heaviest weights they each are able to lift are equal. 
Call two people equally strong if their strongest arms are equally strong (the strongest 
arm can be either left or right), and so are their weakest arms."""

def areEquallyStrong(a_left, a_right, b_left, b_right):
    a_arms = sorted([a_left, a_right])
    b_arms = sorted([b_left, b_right])

    return a_arms == b_arms

"""Determine if a given number is a power of two."""
def powerOfTwo(n):
    return n > 0 and (n & (n-1)) == 0

"Given a non-negative integer n, count the number of 1's in its binary representation."
def countBits(n):
    return bin(n).count('1')

"""Given an integer, return its base 7 string representation."""
def convertToBase7(n):
    if n == 0:
        return 0
    negative = n < 0
    n = abs(n)
    digits = []
    while n:
        digits.append(str(n%7))
        n //= 7
    result = ''.join(reversed(digits))
    return "-" + result if negative else result

"""Given an integer num, repeatedly add all its digits until the result has only one digit, and return it."""

def addDigits(n):
    return sum([int(el) for el in str(n)])


"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array."""
def missingNumber(arr):
    n = len(arr)
    expected = n*(n+1)//2
    return expected - sum(arr)
    