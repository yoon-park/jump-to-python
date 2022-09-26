# 모듈 사용 방법

"""
1. 같은 디렉터리에 존재하기
c:/Users/Jiyoon Park/myworkspace/studying-python/08장 종합문제
디렉터리에 모듈을 불러오고 싶은 파일과 모듈이 함께 존재하면 된다.
"""

"""
2. sys 모듈 사용하기
sys.path에 mymod가 존재하는 디렉터리를 추가해주면 다른 파일에서도 해당 모듈을 사용할 수 있다.
"""
import sys
sys.path.append("c:/Users/Jiyoon Park/myworkspace/studying-python/08장 종합문제")
import mymod

"""
3. PYTHONPATH 환경 변수 사용하기
PYTHONPATH에 mymod가 존재하는 디렉터리를 지정해주면 다른 파일에서도 해당 모듈을 사용할 수 있다.

C:\\Users\Jiyoon Park>set PYTHONPATH=c:\\Users\Jiyoon Park\myworkspace\studying-python\08장 종합문제
"""
