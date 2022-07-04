# 파일 읽고 쓰기
f1 = open("c:/Users/Jiyoon Park/myworkspace/studying-python/04장 연습문제/test.txt", "r")
data = f1.read()
data = data.replace("java", "python")  # 2장 Q05에서 봤듯이, 문자열은 replace한 결과를 다시 저장해줘야 한다
f1.close()

f2 = open("c:/Users/Jiyoon Park/myworkspace/studying-python/04장 연습문제/test.txt", "w")
f2.write(data)
f2.close()
