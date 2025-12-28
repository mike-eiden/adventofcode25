
def turn_left(current, delta):
    extra_zeros = int(delta/100)
    result = current - (delta % 100)
    if result < 0:
        result += 100
        if current != 0:
            extra_zeros += 1
    elif result == 0:
        extra_zeros += 1

    return result, extra_zeros


def turn_right(current, delta):
    extra_zeros = int(delta/100)
    result = current + (delta % 100)
    if result > 99:
        result -= 100
        extra_zeros += 1

    return result, extra_zeros


# seq is a tuple where the first element is a boolean isLeft and the second element is the delta
def check_sequence_for_zeros(seq, initial_start):
    num_zeros = 0
    starting_point = initial_start
    for isLeft, delta in seq:
        if isLeft:
            result = turn_left(starting_point, delta)
            starting_point = result[0]
            num_zeros += result[1]
        else:
            result = turn_right(starting_point, delta)
            starting_point = result[0]
            num_zeros += result[1]

        # the condition where the dial ends on zero is now also captured in the turn functions with extra_zeros
        # if starting_point == 0:
        #     num_zeros += 1

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
