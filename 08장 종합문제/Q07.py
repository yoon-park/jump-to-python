# 한 줄 구구단

dan = input("구구단을 출력할 숫자를 입력하세요(2~9): ")

for i in range(1,10):
	print(i*int(dan), end=' ')	# 한 줄에 결괏값을 계속 이어서 출력하려면 매개변수 end를 사용해 끝 문자를 지정해야 한다