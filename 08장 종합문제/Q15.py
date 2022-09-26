# Duplicate Numbers

def DuplicateNumbers(data):
	result = []
	for num in data:
		if num not in result:	# 중복되지 않는 숫자가 나오는 경우 'result' 리스트에 더한다
			result.append(num)
		else:	# 중복되는 숫자가 나오는 경우 False
			return False
	return len(result) == 10	# 'result' 리스트의 길이가 10일 경우 True, 10이 아닐 경우 False

print(DuplicateNumbers("0123456789"))	# True
print(DuplicateNumbers("01234"))	# False
print(DuplicateNumbers("01234567890"))	# False
print(DuplicateNumbers("6789012345"))	# True
print(DuplicateNumbers("012322456789"))	# False