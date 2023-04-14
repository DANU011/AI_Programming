import random

# 1. 파일 읽어서 뭔가 만들어 냄.
# 2. 그 뭔가로 초기값을 생성함.
# 3. Convex.txt 파일의 수식과 값을 이용해서 계산
def create_problem(filename):

    ini_file = open(filename, 'r')
    expression = ini_file.readline().strip()
    var_names = []
    low = []
    up = []

    for line in ini_file.readlines():
        var_names.append(line.split(",")[0])
        low.append(float(line.split(",")[1]))
        up.append(float(line.split(",")[2]))

    ini_file.close()
    domain = [var_names, low, up]
    return (expression, domain)

def random_init(p):
    expression, domain = p
    init = []
    for i in range(0, len(domain[0])):
        # 최대 최소 사이의 램덤 값
        init.append(random.uniform(domain[1][i], domain[2][i]))

    return init

def evaluate(state, p):
    num_eval=0
    expression, _ = p
    var_name = p[1][0]
    
    for i in range(len(var_name)):
        assignment = var_name[i] + '=' + str(state[i])
        exec(assignment) # exec 스트링으로 된 파이썬의 문자열이 실행 문장이 들어감.

    return eval(expression) # eval 값이 아니라고 생각하는건 무조건 배제

if __name__ == "__main__":
    pass

# # First-choice (simple) hill climbing
# # 간단한 언덕 등반 알고리즘
# ## > Convex.txt 를 사용해서 계산
# ## 1. 파일을 읽어보자
#
# def create_problem(filename): # 파이썬은 함수명에 대문자써서 붙여쓰지 않음 그냥 언더바로 쓴다.
#     # 1-1. 파일을 읽자
#     ini_file = open(filename, 'r')
#     expression = ini_file.readline().strip() # 개행 없애주기 # 한줄 읽고나면 커서는 다음을 넥스트로 가르키고 있음.
#     # 모르겠으면 일단 리스트로 만들어줌.
#     var_names = []
#     low = []
#     up = []
#     # for
#     for line in ini_file.readlines():
#         # n,l,u = tuple(line.split(",")[0])
#         var_names.append(line.split(",")[0])
#         low.append(float(line.split(",")[1]))
#         up.append(float(line.split(",")[2]))
#     ini_file.close()
#     domain=[var_names, low, up]
#
#     return expression, domain
#     # pass
#
# if __name__ == "__main__": # main이 없으면 나를 실행시켜줘
#     # print(create_problem("./data/Convex.txt"))
#     pass
#
# # def inc(x):
# #     return x+1
# #
# # def test_answer():
# #     assert inc(3) == 5

