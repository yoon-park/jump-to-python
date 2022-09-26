# 평균값 구하기

sum = 0

f1 = open("c:/Users/Jiyoon Park/myworkspace/studying-python/08장 종합문제/sample.txt", 'r')
lines = f1.readlines()
f1.close()

f2 = open("c:/Users/Jiyoon Park/myworkspace/studying-python/08장 종합문제/result.txt", 'w')
for line in lines:
	sum += int(line)
avg = sum / len(lines)	# 단순히 줄의 숫자를 세서 넣어줘도 되지만, 리스트의 길이를 사용할 수 있다
f2.write(str(avg))	# avg는 int형이지만, 파일에 쓸 수 있는건 str형이다
f2.close()