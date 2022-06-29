# while문
a = 0
while a < 5:
    a += 1
    cnt = 0
    while cnt < a:
        print("*", end="")  # *을 한개 print하고 다음 줄로 넘어가는 것을 방지하기 위함이다
        cnt += 1
    print("")  # 한 줄이 끝나면 줄을 바꿔줘야 한다는 의미이다

"""
놀랍게도 변수 한개로 풀이 가능하다

i = 0
while True:
    i += 1
    if i > 5: break
    print('*' * i)

파이썬은 '문자열 곱하기'가 가능함을 잊지 말자
"""
