# Sample Programming Language

from types import NoneType
from typing import Iterator, List

class spl_argument:
	def __init__(self, value=None, arg_type:type=NoneType) -> None:
		self.value = value
		if arg_type != None:
			self.arg_type = arg_type
		else:
			self.arg_type = arg_type
	value = None
	arg_type:type = NoneType

class spl_object:
	def __init__(self, key:str, args:List[spl_argument] = []) -> None:
		self.key = key
		self.args= args
	key:str = ""
	args:List[spl_argument] = []
	def __iter__(self) -> Iterator[spl_argument]:
		return iter(self.args)
	def append(self, element:spl_argument) -> None:
		self.args.append(element)

class spl_programm:
	def __init__(self, content:List[spl_object] = []) -> None:
		self.content = content
	content:List[spl_object] = []
	def __iter__(self) -> Iterator[spl_object]:
		return iter(self.content)
	def append(self, element:spl_object) -> None:
		self.content.append(element)

