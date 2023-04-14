import numeric

def test_create_problem():
    result = numeric.create_problem("./data/Convex.txt")
    test_case1 = result[0]
    test_case2 = (len(result[1]), len(result[1][0]))
    test_case1_1 = "(x1 - 2) ** 2 +5 * (x2 - 5) ** 2 + 8 * (x3 + 8) ** 2 + 3 * (x4 + 1) ** 2 + 6 * (x5 - 7) ** 2"
    test_case2_1 = (3,5)
    assert test_case1 == test_case1_1
    assert test_case2 == test_case2_1

    # assert 단언문
    # test_case2 = app.create_problem("./data/Convex.txt")#[0:-1] # 개행문자 없애주기 but 지워주는건 별로...