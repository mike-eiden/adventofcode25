from day1.day1_1 import turn_left
from day1.day1_1 import turn_right
from day1.day1_1 import check_sequence_for_zeros
from day1.day1_1 import parse_input


def test_turn_left_pass_1():
    assert turn_left(50, 68) == 82
    assert turn_left(82, 30) == 52
    assert turn_left(0, 5) == 95
    assert turn_left(55, 55) == 0
    assert turn_left(0, 1) == 99
    assert turn_left(99, 99) == 0
    assert turn_left(14, 82) == 32
    assert turn_left(99, 100) == 99
    assert turn_left(0, 200) == 0
    assert turn_left(0, 201) == 99
    assert turn_left(99, 599) == 0


def test_turn_right_pass_1():
    assert turn_right(52, 48) == 0
    assert turn_right(95, 60) == 55
    assert turn_right(0, 14) == 14
    assert turn_right(0, 114) == 14
    assert turn_right(0, 555) == 55
    assert  turn_right(52, 948) == 0


def test_check_sequence_for_zeros_1():
    test_sequence = [(True, 68), (True, 30), (False, 48), (True, 5), (False, 60), (True, 55), (True, 1), (True, 99), (False, 14), (True, 82)]
    assert check_sequence_for_zeros(test_sequence, 50) == 3


def test_parse_input_1():
    assert parse_input('../day1/sample_input.txt') == [(True, 68), (True, 30), (False, 48), (True, 5), (False, 60), (True, 55), (True, 1), (True, 99), (False, 14), (True, 82)]


def test_parse_input_2():
    assert parse_input('../day1/sample_input_3_digits.txt') == [(True, 68), (False, 303), (True, 30), (False, 48), (True, 5), (False, 60), (True, 55), (True, 1), (True, 99), (False, 14), (True, 82), (True, 400)]


def test_parse_and_check_1():
    assert check_sequence_for_zeros(parse_input('../day1/sample_input.txt'), 50) == 3
