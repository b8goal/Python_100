Sentence = str(input())

for i in range(len(Sentence)):
    print(Sentence[len(Sentence) - i - 1],end = '')

print()
print(Sentence[::-1])