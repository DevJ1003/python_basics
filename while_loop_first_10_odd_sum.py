sum = 0
n = 0

while n <= 20:
    if n % 2 != 0:
        sum = sum + n
    n = n + 1
print("The sum of 10 odd digits: ", sum)