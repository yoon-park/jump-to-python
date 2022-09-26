# 역순 저장

f1 = open("c:/Users/Jiyoon Park/myworkspace/studying-python/08장 종합문제/abc.txt", 'r')
lines = f1.readlines()	# readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다
lines.reverse()	# reverse 함수는 리스트를 역순으로 뒤집어 준다
f1.close()

f2 = open("c:/Users/Jiyoon Park/myworkspace/studying-python/08장 종합문제/abc.txt", 'w')
for line in lines:
	line = line.strip()	# strip 함수는 문자열 양쪽에 있는 한 칸 이상의 연속된 공백을 모두 지운다 -> 포함되어있는 줄바꿈 문자를 제거하기 위해 사용
	f2.write(line)
	f2.write('\n')
f2.close()