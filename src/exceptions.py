class CustomException(Exception):

    def __init__(self, message):
        self.message = message


class InvalidLengthReorganizationException(CustomException):

    def __init__(self, length, necessary_length):
        message = 'Invalid length of the reorganization = {}. Necessary: {}'.format(length, necessary_length)

        super().__init__(message)


class InvalidReorganizationException(CustomException):

    def __init__(self):
        message = 'Invalid the reorganization. The sequence must be without repetitions and have positive elements'

        super().__init__(message)


class InvalidCountCoachesException(CustomException):

    def __init__(self, count, max_count):
        message = 'Invalid count of the coaches = {}.'
        message += ' The count of the coaches mush be positive and less than or equal to {}'

        message.format(count, max_count)

        super().__init__(message)
