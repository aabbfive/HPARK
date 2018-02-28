class Keyword(object):
	def __init__(self, value):
		if type(value) == type(self):
			self.pattern = value.pattern
			self.value = value.value
		else:
			self.pattern = re.escape(value)
			self.value = value
	def __str__(self):
		return self.pattern
	def __repr__(self):
		return 'Keyword(value={}, pattern={})'.format(self.value, self.pattern)
class Keywords(object):
	def __init__(self, _keywords):
		keywords = list(map(Keyword, _keywords))
		self.__data		= list(sorted(keywords, key=lambda dat: dat.value, reverse=True))
		self.__rules_p 	= list(map(lambda keyword: keyword.pattern, self.__data))
		self.__rules_v	= list(map(lambda keyword: keyword.value, self.__data))
	def contains(self, item):
		return item in self.__rules_v
	def getRule(self, item):
		return list(filter(lambda item: item.value == item, self.__data))[0]
	def get(self, state=False):
		if state:
			return ('|'.join(self.__rules_p))
		return self.__rules_p
	def __repr__(self):
		return "Keywords({})".format(self.__data)