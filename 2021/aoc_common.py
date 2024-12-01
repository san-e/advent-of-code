def get_input(path: str) -> list:
    with open(path, "r") as f:
        input = f.read().split("\n")
    return input

def get_test_input(path: str) -> tuple:
    input = get_input(path)

    test_answer = input[-1:][0]
    test_input = input[:-2]

    return test_input, test_answer

def test(index: int, path: str, test_function, *args):
    test_input, test_answer = get_test_input(path)
    assert str(test_function(test_input, *args)) == test_answer
    print(f"Test {index} passed")
