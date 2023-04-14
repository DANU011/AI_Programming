import app

def test_create_problem():
    assert app.create_problem("./data/Conbex.txt") == ""