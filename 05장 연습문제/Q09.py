# 라이브러리 sys
import sys

sum = 0
for i in sys.argv[1:]:  # sys.argv 리스트는 파일 이름도 0번째 요소로 포함하고 있으므로 이를 제외시켜줘야 한다
    sum += int(i)  # sys.argv 리스트에는 요소들이 문자로 저장되므로 int를 이용해 숫자로 바꿔줘야한다

print(sum)
