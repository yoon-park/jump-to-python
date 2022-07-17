# 구구단
def GuGu(dan):
    result = []
    i = 0
    while i < 9:
        result.append(dan * (i + 1))
        i += 1
    return result  # 아무래도 이 경우에는 함수 내부에서 print하는 것 보단 return으로 결과값을 돌려주는 편이 좋은듯


print(GuGu(2))
