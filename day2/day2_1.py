
def check_same_digits(first_half, second_half):
    count = 0
    for char in first_half:
        if char != second_half[count]:
            return False
        count += 1

    return True


def iterate_id_range(id_range):
    range_split = id_range.split('-')
    str_range_start = range_split[0]
    str_range_end = range_split[1]

    invalid_ids_count = 0
    sum_invalid_ids = 0

    for i in range(int(str_range_start), (int(str_range_end) + 1)):
        digits = len(str(i))
        if digits % 2 == 0:
            mid = int(digits/2)
            if check_same_digits(str(i)[0:mid], str(i)[mid:]):
                invalid_ids_count += 1
                sum_invalid_ids += i

    return invalid_ids_count, sum_invalid_ids


def parse_input(filename):
    ranges = []
    f = open(filename)
    data = f.readlines()
    for line in data:
        ranges = line.split(',')

    return ranges
