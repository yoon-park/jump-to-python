# 하위 디렉터리 검색하기
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)	# 해당 디렉터리에 있는 파일들의 리스트
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)	# 파일 이름에 dirname을 앞에 덧붙여 경로를 포함시켜준다
            if os.path.isdir(full_filename):    # 풀네임이 파일인지 디렉터리인지 분간해준다
                search(full_filename)   # 만약 디렉터리라면, 재귀함수를 호출한다
            else:
                ext = os.path.splitext(full_filename)[-1]   # 파일 이름을 확장자를 기준으로 두 부분으로 나눠준다
                if ext == '.py': 
                    print(full_filename)
    except PermissionError: # 권한이 없는 디렉터리에 접근하였을 경우
        pass

search("c:/")

"""
일반적으로, 시작 디렉터리부터 하위 모든 디렉터리를 차례대로 방문하고 싶을 때에는 os.walk 함수를 사용한다.

import os

for (path, dir, files) in os.walk("c:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))
"""