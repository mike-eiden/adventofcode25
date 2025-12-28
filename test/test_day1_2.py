from day1.day1_2 import turn_left
from day1.day1_2 import turn_right
from day1.day1_2 import check_sequence_for_zeros


def test_turn_left():
    assert turn_left(50, 68) == (82, 1)
    assert turn_left(50, 168) == (82, 2)
    assert turn_left(1, 2) == (99, 1)
    assert turn_left(1, 1) == (0, 1)
    assert turn_left(1, 301) == (0, 4)
    assert turn_left(0, 5) == (95, 0)
    assert turn_left(1, 6) == (95, 1)
    assert turn_left(99, 4) == (95, 0)


def test_turn_right():
    assert turn_right(95, 60) == (55, 1)
    assert turn_right(0, 1000) == (0, 10)
    assert turn_right(99, 1) == (0, 1)
    assert turn_right(99, 2) == (1, 1)
    assert turn_right(98, 1) == (99, 0)
    assert turn_right(98, 2) == (0, 1)
    assert turn_right(98, 3) == (1, 1)
    assert turn_right(98, 402) == (0, 5)
    assert turn_right(98, 103) == (1, 2)


def test_check_sequence():
    test_sequence = [(True, 68), (True, 30), (False, 48), (True, 5), (False, 60), (True, 55), (True, 1), (True, 99), (False, 14), (True, 82)]
    assert check_sequence_for_zeros(test_sequence, 50) == 6
    test_sequence_2 = [(True, 68), (True, 30), (False, 48), (True, 5), (False, 60), (True, 55), (True, 1), (True, 99),
                     (False, 14), (True, 82), (True, 333)]
    assert check_sequence_for_zeros(test_sequence_2, 50) == 10
