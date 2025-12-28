
def turn_left(current, delta):
    result = current - (delta % 100)
    if result < 0:
        result += 100

    return result


def turn_right(current, delta):
    result = current + (delta % 100)
    if result > 99:
        result -= 100

    return result


# seq is a tuple where the first element is a boolean isLeft and the second element is the delta
def check_sequence_for_zeros(seq, starting_point):
    num_zeros = 0
    for isLeft, delta in seq:
        if isLeft:
            starting_point = turn_left(starting_point, delta)
        else:
            starting_point = turn_right(starting_point, delta)

        if starting_point == 0:
            num_zeros += 1

    return num_zeros


def parse_input(filename):
    puzzle_input = []
    f = open(filename)
    data = f.readlines()
    for line in data:
        isLeft = False
        if line[0] == 'L':
            isLeft = True

        if line[-1] == '\n':
            temp_tuple = (isLeft, int(line[1:-1]))
        else:
            temp_tuple = (isLeft, int(line[1:]))

        puzzle_input.append(temp_tuple)

    return puzzle_input
