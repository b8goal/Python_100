numbers = list(map(int,input().strip().split()))

len1 = len(numbers) - 1

for i in range(len1,-1,-1):
    print(numbers[i], end=' ')