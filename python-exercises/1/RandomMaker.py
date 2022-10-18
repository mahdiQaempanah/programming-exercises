import random
import string


class RandomMaker:
    @staticmethod
    def random_number(start_length, end_length):
        length = random.randint(start_length, end_length)
        return int(''.join([str(random.randint(1, 9) if i == 0 else random.randint(0, 9)) for i in range(length)]))

    @staticmethod
    def random_name(start_length, end_length):
        length = random.randint(start_length, end_length)
        return ''.join([random.choice(string.ascii_letters) for _ in range(length)])
