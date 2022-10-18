from BaseEntity import BaseEntity
from RandomMaker import RandomMaker


class Street(BaseEntity):

    def to_json(self, number_of_entity):
        return super().to_json(number_of_entity)

    def to_cmv(self, number_of_entity):
        return super().to_cmv(number_of_entity)

    def make_random_info(self):
        ret = dict()
        ret['city'] = RandomMaker.random_name(5, 15)
        ret['district'] = RandomMaker.random_number(4, 7)
        return ret
