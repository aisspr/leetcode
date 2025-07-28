# Format 1: Array on one line
arr = list(map(int, input().split()))

# Format 2: Matrix with dimensions
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Format 3: Multiple test cases
t = int(input())
for _ in range(t):
    line = input().strip()