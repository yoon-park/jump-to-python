# 탭을 4개의 공백으로 바꾸기
import sys

tab = sys.argv[1]
space = sys.argv[2]

f = open(tab, "r")
tab_text = f.read()
space_text = tab_text.replace("\t", " " * 4)
# 문자열 이스케이프 코드로 tab을 표현하는 방법은 '\t'이다, 문자열 곱하기도 잊지 말 것!
f.close()

f = open(space, "w")
f.write(space_text)
f.close()
