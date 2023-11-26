from src.exceptions import InvalidLengthReorganizationException


class Train:

    def __init__(self, count_coaches):
        self._count_coaches = count_coaches

    def get_count_coaches(self):
        return self._count_coaches


class Reorganization:

    def __init__(self, sequence):
        self._sequence = sequence
        self._length = len(sequence)

    def __len__(self):
        return self._length

    def __getitem__(self, item):
        return self._sequence[item]


class Reorganizer:

    def __init__(self, train, reorganisations):
        self._train = train
        self._reorganizations = reorganisations

    def get_results(self):
        results = []

        count_coaches = self._train.get_count_coaches()

        for reorganization in self._reorganizations:
            if count_coaches != len(reorganization):
                raise InvalidLengthReorganizationException(len(reorganization), count_coaches)

            is_possible_reorganization = self._is_possible_reorganization(reorganization)

            results.append(is_possible_reorganization)

        return results

    def _is_possible_reorganization(self, reorganization):
        for i in range(0, len(reorganization) - 1):
            if abs(reorganization[i + 1] - reorganization[i]) == 1:
                continue

            if reorganization[i] > reorganization[i + 1]:
                return False

        return True
