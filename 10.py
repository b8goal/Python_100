InputStarCount = int(input())

for i in range(1, InputStarCount+1):
    print(' ' * (InputStarCount-i), '*' * (2*i-1))