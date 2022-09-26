# DashInsert 함수

def DashInsert(data):
    numbers = list(map(int, data))  # 'data' 문자열을 int형 리스트인 'numbers'로 변경
    result = []

    for i, num in enumerate(numbers):   # 파이썬의 for문에서 인덱스번호를 사용하고 싶을 때, enumerate를 사용
        result.append(str(num)) # 'result' 리스트에 num을 str형으로 저장
        if i < len(numbers) - 1:    # 'numbers'에 다음 수가 존재할때만
            if num % 2 == 1 and numbers[i+1] % 2 == 1:  # 현재 수도 다음 수도 홀수일 때
                result.append("-")  # 두 수 사이에 '-' 추가
            elif num % 2 != 1 and numbers[i+1] % 2 != 1: # 현재 수도 다음 수도 짝수일 때
                result.append("*")  # 두 수 사이에 '*' 추가

    print("".join(result))  # str형 리스트를 문자열로 출력하기 위한 방법(?)

DashInsert("4546793")