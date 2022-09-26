# 모스 부호 해독

dic = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F', '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L', '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R', '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X', '-.--':'Y','--..':'Z'}	# 모스 부호를 딕셔너리에 저장

def morse(src):
	result = []
	for word in src.split("  "):	# 공백 2개를 만나면 단어 구분
		for char in word.split(" "):	# 공백 1개를 만나면 문자 구분
			result.append(dic[char])	# 문자를 해독하여 result 리스트에 더하기
		result.append(" ")	# 한 단어가 끝날 때 공백 추가
	return "".join(result)	# 리스트를 문자열로 바꿔주는 방법

sentence = input("모스 부호를 입력하세요: ")	# Q14에서와 같이, 문자열은 리스트로 변환할 필요가 없다
print(morse(sentence))

# print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--')) -> HE SLEEPS EARLY