# 오류와 예외 처리

result = 0

try:
    [1, 2, 3][3]	# IndexError -> 여기서 에러 감지돼서 바로 except로 이동
    "a"+1	# TypeError
    4 / 0	# ZeroDivisionError
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3	# result = 3
finally:
    result += 4	# result = 7

print(result)	# 7