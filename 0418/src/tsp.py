import random
import math

# 여러분이 작성 가능
# 읽기 좋게!

def create_problem(filename):
    f = open(filename, "r")
    num_cities = int(f.readline())

    locations = []
    for line in f.readlines():
        # 튜플(x,y)
        locations.append(eval(line))

    f.close()
    table = create_distance_table(num_cities, locations)
    return num_cities, locations, table

# 그래프는 어떻게 표현하죠?
# 인접행렬을 만들어야함. 좌표와 갯수 필요
# TODO : 인접행렬 그래프 만들고 다시
def create_distance_table(num_cities, locations):

    # 이건 뭐 어떻게 하나?
    # 1) 거리도 계산해야 하는데...
    # 맨하튼? => 격자(grid world) - 유클리드 거리...
    # - 잠 두 개가 필요?
    table = []
    for i in range(num_cities):
        line = []
        for k in range(num_cities):
            # ((locations[i][0] - locations[k][0]**2)+(locations[i][1] - locations[k][1]**2))
            distance = math.sqrt(((locations[i][0] - locations[k][0]**2)+(locations[i][1] - locations[k][1]**2)))
            line.append(distance)
        table.append(line)
        pass

    return table

def random_init(p):
    # 결과 shuffle!
    n = p[0]
    init=list(range(n))
    random.shuffle(init) 
    return(init)

def evaluate(current,p):
    # cost 출력
    cost = 0
    num_cities, locations, table = p
    for i in range(num_cities):
        cost += table[current[i]][current[i-1]]
    return cost

def describe_problem(p):
    print()
    n = p[0]
    print(f"Number of citeis : {n}")
    locations = p[1]
    # table = p[2]
    for i in range(n):
        print(f"{locations[i]}")
        if i%5 == 4:
            print()
        
    pass

if __name__ == "__main__":
    p = create_problem("../data/tsp30.txt")
    init = random_init(p)
    print(evaluate(init, p))

