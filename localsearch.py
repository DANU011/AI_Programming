#  First-choice (simple) hill climbing
# 간단한 언덕 등반 알고리즘
## > Convex.txt 를 사용해서 계산
## 1. 파일을 읽어보자

def create_problem(filename): # 파이썬은 함수명에 대문자써서 붙여쓰지 않음 그냥 언더바로 쓴다.
    # 1-1. 파일을 읽자
    ini_file = open(filename, 'r')
    expression = ini_file.readline()
    # 1-2. 수식과 리스트로 분리
    # 1-3. 리턴!!
    return expression, # domain
    # pass

if __name__ == "__main__": # main이 없으면 나를 실행시켜줘
    print(create_problem("./data/Convex.txt"))