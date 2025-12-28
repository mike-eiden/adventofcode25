#from day1.day1_2 import parse_input
# from day1.day1_2 import check_sequence_for_zeros
from day2.day2_1 import parse_input
from day2.day2_1 import iterate_id_range

# def day1():
#     sequence = parse_input('day1/my_puzzle_input.txt')
#     num_zeros = check_sequence_for_zeros(sequence, 50)
#     print(num_zeros)


def day2():
    ranges = parse_input('day2/my_id_inputs.txt')
    invalid_ids_count = 0
    invalid_ids_sum = 0
    for id_range in ranges:
        result = iterate_id_range(id_range)
        invalid_ids_count += result[0]
        invalid_ids_sum += result[1]
    print(invalid_ids_sum)


if __name__ == '__main__':
    # day1()
    day2()
