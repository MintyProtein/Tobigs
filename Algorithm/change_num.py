import sys
nums = []
while True:
    num = sys.stdin.readline().strip()
    if num == '0': break
    else: nums.append(num)
for num in nums:
    if num == num[::-1]: print("yes")
    else: print("no")