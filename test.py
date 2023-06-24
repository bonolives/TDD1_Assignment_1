# Test First TDD Cycle 1

# Writing first test


def test1_multiply():
    assert multiply(1, 1) == 1


# Writing a multiply function to get the test to pass


# def multiply(a, b):
# return a * b

# Test First TDD Cycle 2

# writing Second Test


def test2_multiply():
    assert multiply(2, 2) == 4


# updating the multiply function to pass test 2 but making sure test 1 passes too


def multiply(a, b):
    return a * b
