import sys

U, D, H = map(int, sys.stdin.readline().split(' '))
H -= 1
dy = U - D
n = (H - U) // dy
if H - n * dy > 0: n +=1
n += 1
print(n)