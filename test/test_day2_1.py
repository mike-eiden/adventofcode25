from day2.day2_1 import check_same_digits
from day2.day2_1 import iterate_id_range
from day2.day2_1 import parse_input


def test_check_same_digits_pass():
    assert check_same_digits('123', '123') is True
    assert check_same_digits('11', '11') is True
    assert check_same_digits('1188511885', '1188511885') is True


def test_check_same_digits_fail():
    assert check_same_digits('123', '124') is False
    assert check_same_digits('234', '123') is False


def test_iterate_id_range():
    assert iterate_id_range('11-22') == (2, 33)
    assert iterate_id_range('11-21') == (1, 11)
    assert iterate_id_range('11-101') == (9, 495)
    assert iterate_id_range('11-1010') == (10, 1505)
    assert iterate_id_range('101-102') == (0, 0)
    assert iterate_id_range('95-115') == (1, 99)
    assert iterate_id_range('998-1012') == (1, 1010)
    assert iterate_id_range('1188511880-1188511890') == (1, 1188511885)
    assert iterate_id_range('222220-222224') == (1, 222222)
    assert iterate_id_range('1698522-1698528') == (0, 0)
    assert iterate_id_range('446443-446449') == (1, 446446)
    assert iterate_id_range('38593856-38593862') == (1, 38593859)
    assert iterate_id_range('565653-565659') == (0, 0)
    assert iterate_id_range('824824821-824824827') == (0, 0)
    assert iterate_id_range('2121212118-2121212124') == (0, 0)


def test_parse_input():
    sample_ranges = ['11-22','95-115','998-1012','1188511880-1188511890','222220-222224','1698522-1698528','446443-446449','38593856-38593862','565653-565659','824824821-824824827','2121212118-2121212124']
    assert parse_input('../day2/sample_input.txt') == sample_ranges


def test_sum_input():
    ranges = parse_input('../day2/sample_input.txt')
    invalid_count = 0
    invalid_sum = 0
    for id_range in ranges:
        result = iterate_id_range(id_range)
        invalid_count += result[0]
        invalid_sum += result[1]

    assert invalid_sum == 1227775554
