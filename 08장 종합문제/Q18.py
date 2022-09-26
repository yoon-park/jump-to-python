# 문자열 검색

import re

p = re.compile("[a-z]+")
"""
[a-z] : 소문자 전체
+ : 최소 한번 이상 반복
"""
m = p.search("5 python")	# search() 메서드 : 문자열 전체를 검색하여 정규식과 매치되는지 조사

print(m) # <re.Match object; span=(2, 8), match='python'>
print(m.start() + m.end()) # 2 + 8 = 10