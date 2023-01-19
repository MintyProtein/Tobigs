import sys
N = int(sys.stdin.readline())
directions = list(sys.stdin.readline().strip().split(' '))
position = [1, 1]
for d in directions:
    if d == 'U':
        dx = -1
        dy = 0
    elif d == 'D':
        dx = 1
        dy = 0
    elif d == 'L':
        dx = 0
        dy = -1
    elif d == 'R':
        dx = 0
        dy = 1
    
    if (position[0]+dx > N) or (position[0]+dx < 1 ) or (position[1]+dy > N) or (position[1]+dy < 1):
        continue
    else:
        position[0] += dx
        position[1] += dy
print(position[0], position[1])