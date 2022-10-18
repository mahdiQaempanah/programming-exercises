from BaseEntity import BaseEntity
from RandomMaker import RandomMaker


class Student(BaseEntity):

    def to_json(self, number_of_entity):
        return super().to_json(number_of_entity)

    def to_cmv(self, number_of_entity):
        return super().to_cmv(number_of_entity)

    def make_random_info(self):
        ret = dict()
        ret['first_name'] = RandomMaker.random_name(5, 15)
        ret['last_name'] = RandomMaker.random_name(5, 15)
        ret['id'] = RandomMaker.random_number(10, 10)
        ret['phone_number'] = RandomMaker.random_number(11, 11)
        return ret
