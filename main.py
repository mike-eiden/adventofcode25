from day1.day1_2 import parse_input
from day1.day1_2 import check_sequence_for_zeros

if __name__ == '__main__':
    sequence = parse_input('day1/my_puzzle_input.txt')
    num_zeros = check_sequence_for_zeros(sequence, 50)
    print(num_zeros)
