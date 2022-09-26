# 숫자의 총합 구하기

num = input("더하고 싶은 숫자들을 입력하세요: ")
nlist = num.split(",")
sum = 0

for i in nlist:
	sum += int(i)

print(sum)