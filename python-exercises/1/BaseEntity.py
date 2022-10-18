import json
from abc import abstractmethod, ABC


class BaseEntity(ABC):

	@abstractmethod
	def to_json(self, number_of_entity):
		entities = [self.make_random_info() for _ in range(number_of_entity)]
		return str(json.dumps(entities))

	@abstractmethod
	def to_cmv(self, number_of_entity):
		entities = [self.make_random_info() for _ in range(number_of_entity)]
		ret = [','.join(entities[0].keys())]
		for i in entities:
			ret.append(','.join(map(str, i.values())))
		return '\n'.join(ret)

	@abstractmethod
	def make_random_info(self):
		pass

