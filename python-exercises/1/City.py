from BaseEntity import BaseEntity
from RandomMaker import RandomMaker


class City(BaseEntity):

    def to_json(self, number_of_entity):
        return super().to_json(number_of_entity)

    def to_cmv(self, number_of_entity):
        return super().to_cmv(number_of_entity)

    def make_random_info(self):
        ret = dict()
        ret['name'] = RandomMaker.random_name(5, 15)
        ret['area'] = RandomMaker.random_number(7, 10)
        ret['country'] = RandomMaker.random_name(5, 15)
        return ret
