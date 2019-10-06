kor, math, eng = map(int, input().split())

avg_subject = (kor+math+eng)/3

print(int(avg_subject))

subjects = list(map(int, input().split()))
print(int(sum(subjects)/3))