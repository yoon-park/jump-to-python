# 문자열 압축하기

data = input("문자열을 입력하세요: ")	# 문자열은 리스트로 변한하지 않아도 되는 것으로 밝혀져!!!
result = []
cnt = 1

for i, c in enumerate(data):
	if i < len(data) - 1:	# 'data' 문자열에 다음 글자가 존재할 때
		if c == data[i+1]:	# 현재 글자와 다음 글자가 일치한다면
			cnt += 1
		else:	# 현재 글자와 다음 글자가 일치하지 않는다면
			result.append(c)
			result.append(str(cnt))
			cnt = 1
	else:	# 'data' 문자열의 마지막 글자일 경우
		result.append(c)
		result.append(str(cnt))

print("".join(result))