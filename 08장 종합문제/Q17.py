# 기초 메타 문자

import re	# 파이썬에서 정규 표현식을 지원하는 모듈

p = re.compile("a[.]{3,}b")
"""
[.] : Dot(.)문자
{m, n} : m~n회 반복
"""

# match() 메서드 : 문자열의 처음부터 정규식과 매치되는지 조사
print(p.match("acccb"))		# None
print(p.match("a....b"))	# <re.Match object; span=(0, 6), match='a....b'> (매치 객체 출력)
print(p.match("aaab"))		# None
print(p.match("a.cccb"))	# None