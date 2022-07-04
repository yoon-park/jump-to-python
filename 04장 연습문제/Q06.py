# 파일에 새로운 내용 추가하기
f = open("c:/Users/Jiyoon Park/myworkspace/studying-python/04장 연습문제/test.txt", "a")
data = input("추가할 내용을 입력하세요: ")
f.write(data)
f.write("\n")  # -> 이것도 추가해주면 새로운 내용을 입력할 때마다 줄을 바꿔주므로 좋다
f.close()
