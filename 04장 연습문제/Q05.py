# 파일 쓰고 읽기
f1 = open("c:/Users/Jiyoon Park/myworkspace/studying-python/04장 연습문제/test.txt", "w")
f1.write("Life is too short")
f1.close()

f2 = open("c:/Users/Jiyoon Park/myworkspace/studying-python/04장 연습문제/test.txt", "r")
print(f2.read())
f2.close()
