import os
import json
from spl_typing import *

if os.path.isfile("settings.json"):
	settings = json.load(open("settings.json"))
else:
	print("No configuration file found.")
	settings = json.load(open("default.json"))

class spl_parser:
	def __init__(self, programm:str, settings:dict) -> None:
		self.programm = programm
		self.settings = settings
	programm:str = ""
	parsed_programm:spl_programm
	def spl_parse(self) -> spl_programm:
		output = []
		key = ""
		args = []
		word = ""
		# 
		is_new_line = True
		skip = False
		skip_exit_characters = ""
		# Iterate through the programm
		for letter in self.programm:
			if is_new_line:
				# Check if we are in a comment
				if letter == "#":
					skip = True
					key = "#"
			else:
				if skip:
					if letter in skip_exit_characters:
						skip = False
		self.parsed_programm = spl_programm(output)
		return self.parsed_programm