sum = 0

for i in range(2, 11, 2):
    sum += i
    # i = i+2   // This doesn't work in python
print("The sum of even digits from of 1 to 10: ", sum)