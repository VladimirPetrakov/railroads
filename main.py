from src.entities import Train, Reorganization, Reorganizer
from src.exceptions import CustomException, InvalidCountCoachesException, InvalidReorganizationException


def main():
    reorganizers = build_reorganizers()

    print_reorganizers(reorganizers)


def build_reorganizers():
    reorganizers = []

    is_current_block = False

    train = None
    reorganizations = []

    while True:
        input_line = input()

        if input_line == '0':
            if train is None:
                break

            reorganizer = Reorganizer(train, reorganizations)
            reorganizers.append(reorganizer)

            is_current_block = False

            train = None
            reorganizations = []

            continue

        if is_current_block:
            reorganization_sequence = tuple(map(int, input_line.split()))

            check_valid_reorganization_sequence(reorganization_sequence)

            reorganization = Reorganization(reorganization_sequence)

            reorganizations.append(reorganization)
        else:
            n = int(input_line)

            check_valid_count_coaches(n, 1000)

            train = Train(n)

            is_current_block = True

    return reorganizers


def check_valid_count_coaches(count_coaches, max_count_coaches):
    if count_coaches < 1 or count_coaches > 1000:
        raise InvalidCountCoachesException(count_coaches, max_count_coaches)


def check_valid_reorganization_sequence(sequence):
    for sequence_element in sequence:
        if sequence_element < 1 or sequence.count(sequence_element) > 1:
            raise InvalidReorganizationException()


def print_reorganizers(reorganizers):
    count_reorganizers = len(reorganizers)

    for index, reorganizer in enumerate(reorganizers):
        print_reorganizer(reorganizer)

        if index != count_reorganizers - 1:
            print("\n", end="")


def print_reorganizer(reorganizer):
    result_reorganizations = reorganizer.get_results()

    for result_reorganization in result_reorganizations:
        if result_reorganization:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    try:
        main()
    except CustomException as e:
        print(e.message)
