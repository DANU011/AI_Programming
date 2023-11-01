import tsp

LIMITS = 100

def first_choice(p):
     current = tsp.random_init(p)
     value_distance = tsp.evaluate(current, p)
     i = 0
     while i < LIMITS:
          successor = ramdom_mutant(current,p)
          _value_distance = tsp.evaluate(successor, p)
          if _value_distance < Value_distance:
               current = successor
               Value_distance = _value_distance
               i = 0
          else:
               i += 1
     ## 알고리즘 활용해서 최적값을 변경 코드를 작성
     ## value_distance 이걸 어떻게 줄이나?
     return current, Value_distance

# 이거 변이를 준다는게 말이 안되는거 같은데?
def ramdom_mutant(current, p):
     while True:
        # 일단 좌표는 어떻게 받아옴? 뭐??
        i, j = sorted([random.randrange(p[0]) for _ in range(2)])
        if i < j :
            cur_copy = inversion(current, i, j)
            break
     return cur_copy


def inversion(current, i, j):
     cur_copy = current[:]
     while i < j:
        cur_copy[i], cur_copy[j] = cur_copy[j], cur_copy[i]
        i += 1
        j -= 1
     return cur_copy


if __name__ == "__main__":
    p = tsp.create_problem("./data/tsp30.txt")
    solution, minimum = first_choice(p)
    print(solution)
    print(minimum)
