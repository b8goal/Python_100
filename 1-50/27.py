data_name = list(map(str,input().split()))
data_subject = list(map(int,input().split()))

data_dict = dict(zip(data_name,data_subject))
print(data_dict)