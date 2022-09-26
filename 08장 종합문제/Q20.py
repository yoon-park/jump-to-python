# 전방 탐색

import re

# (?=...) : 긍정형 전방 탐색, ... 에 해당되는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다
p1 = re.compile(".*[@].*[.].*$")	# $ : 문자열의 끝과 매치함
p2 = re.compile(".*[@].*[.](?=com$|net$).*$")	# 이메일 주소가 com이나 net일 경우만 통과된다

print(p1.match("pahkey@gmail.com"))	# 매치 객체 출력
print(p1.match("kim@daum.net"))		# 매치 객체 출력
print(p1.match("lee@myhome.co.kr"))	# 매치 객체 출력

print(p2.match("pahkey@gmail.com"))	# 매치 객체 출력
print(p2.match("kim@daum.net"))		# 매치 객체 출력
print(p2.match("lee@myhome.co.kr"))	# None