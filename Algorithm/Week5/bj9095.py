import sys
t = int(sys.stdin.readline())
inputs = []
for _ in range(t):
    inputs.append(int(sys.stdin.readline()))


def factorial(k):
    temp = 1
    while k > 0:
        temp *= k
        k -= 1
    return temp


for n in inputs:
    count = 0
    num3 = n // 3
    num2 = (n - (3*num3)) // 2
    num1 = n - (3*num3) - (2*num2)
    while num3 > 0 or num2 > 0:
        count += factorial(num3 + num2 + num1) // (factorial(num3) * factorial(num2) * factorial(num1))
        if 0 < num2:
            num2 -= 1
            num1 += 2
            continue
        if 0 < num3:
            num3 -= 1
            num2 = (num1+1) // 2 + 1
            num1 = (num1+1) % 2
    count += factorial(num3 + num2 + num1) // (factorial(num3) * factorial(num2) * factorial(num1))
    print(count)