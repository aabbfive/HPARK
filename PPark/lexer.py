import re, sys, collections
from PPark.constant import *
class Lexer(object):
	
	__rules = []
	__group_type = {}
	
	def __init__(self, rules=[], debug=False, skip_whitespace=True):
		self.debug = debug
		self.skip_whitespace = skip_whitespace
		self.re_ws_skip = re.compile('\S')
		self.__rules = rules
	
	def input(self, buf):
		self.buf = buf
		self.pos = 0
	
	def reset(self):
		self.pos = 0
	
	def addRule(self, name, pattern, action=None):
		if isinstance(pattern, Keywords):
			self.__rules.append(self.__PatternAction(name, pattern.get(True), action))
		elif isinstance(pattern, Keyword):
			self.__rules.append(self.__PatternAction(name, pattern.pattern, action))
		else:
			self.__rules.append(self.__PatternAction(name, pattern, action))
		self.__init()
	
	def __init(self):
		idx = 1
		regex_parts = []

		for token in self.__rules:
			groupname = 'GROUP%s' % idx
			regex_parts.append('(?P<%s>%s)' % (groupname, token.pattern))
			self.__group_type[groupname] = token
			idx += 1
		self.regex = re.compile('|'.join(regex_parts), re.UNICODE)
	
	class LexerError(Exception):
		def __init__(self, pos):
			self.pos = pos
	
	class __PatternAction:
		__slots__ = ('tag', 'pattern', 'action')
		def __init__(self, tag, pattern,  action):
			self.pattern = pattern
			self.action = action
			self.tag = tag
		def __repr__(self):
			return 'PatternAction(tag={}, pattern={}, action={})'.format(self.tag, self.pattern, [None, self.action.__name__][callable(self.action)])
	
	class Token:
		__slots__ = ('value', 'type', 'pos')
		def __init__(self, value, type, pos):
			self.value = value
			self.type = type
			self.pos = pos

		def __repr__(self):
			return 'Token(value=\'{}\', type={}, pos={})'.format(self.value, self.type, self.pos)
	
	def token(self):
		if self.pos >= len(self.buf):
			return None
		else:
			if self.skip_whitespace:
				m = self.re_ws_skip.search(self.buf, self.pos)

				if m:
					self.pos = m.start()
				else:
					return None
			m = self.regex.match(self.buf, self.pos)
			if m:
				val = None
				groupname = m.lastgroup
				funcToken = self.__group_type[groupname]
				tok = self.Token(m.group(groupname), funcToken.tag, self.pos)
				self.pos = m.end()
				if callable(funcToken.action):
					val = funcToken.action(tok)
				return [tok, val][bool(val)]

			# if we're here, no rule matched
			raise self.LexerError(self.pos)

	def __iter__(self):
		return self

	def __next__(self):
		token = self.token()
		if token is not None:
			return token
		raise StopIteration()

	next = __next__ # Python 2 support
	def on_match(self, pattern):
		def decorator(func):
			self.addRule(func.__name__, pattern, func)
			return func
		return decorator