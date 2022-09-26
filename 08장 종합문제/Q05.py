# 피보나치 함수

def fibo(i):
	if i == 0:
		return 0
	if i == 1:
		return 1
	return fibo(i-2) + fibo(i-1)

n = input("정수를 입력하세요: ")

for i in range(int(n)):	# 입력받은 정수는 str 형태이므로 int로 바꿔준다
	print(fibo(i))