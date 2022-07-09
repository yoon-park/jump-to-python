# 내장 함수 all, abs, chr, ord
print(all([1, 2, abs(-3) - 3]))  # 3번째 요소가 0이므로 False
print(chr(ord("a")) == "a")  # 문자 -> 유니코드 -> 문자 이므로 True
