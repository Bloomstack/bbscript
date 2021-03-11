import json
from copy import deepcopy
from .constants import \
	CMD_UNSUPPORTED, \
	CMD_ARRAY
from .stdlib import load_stdlib
from .errors import SyntaxError
from .flags import StopExecutionNoRecover, RepeatStatement

class Runtime:
	def __init__(self, ctx = None, script = None):
		self.ctx = {}
		self.script = []
		# copy user ctx
		if ctx:
			self.ctx.update(ctx)
		# load stdlib ctx
		load_stdlib(self.ctx)
		self.ctx.update({
			"#EXEC_LINE": self.exec_line
		})
		if script:
			self.script = deepcopy(script)

	def load_script(self, script):
		"""Loads a script array"""
		self.script = deepcopy(script)

	def update_context(self, ctx):
		"""Adds extra context data into the runtime context"""
		self.ctx.update(ctx)

	def list_functions(self):
		"""Lists all functions currently loaded in the context"""
		for key in self.ctx.keys():
			if key[0] != "$":
				yield key

	def docs(self):
		"""Generates meta information for all available functions in the context if they expose it."""
		meta = []
		for key, fn in self.ctx.items():
			if key[0] != "$" and hasattr(fn, "bbmeta"):
				meta.append(dict(name=key, meta=fn.bbmeta))

		return json.dumps(meta, default=lambda x: '<not serializable>', indent=2)

	def list_variables(self):
		"""Lists all variables currently in the context"""
		for key in self.ctx.keys():
			if key[0] == "$":
				yield key[1:]

	def exec(self):
		"""Executes the loaded script returning a generator"""
		while len(self.script) > 0:
			line = self.script.pop(0)
			result = self.exec_line(line)
			if isinstance(result, StopExecutionNoRecover):
				print("[Early Exit!]")
				return

			yield

	def exec_line(self, line):
		"""Executes a single line of bbscript"""
		# assert line is an array
		if not isinstance(line, list):
			raise SyntaxError("BBScript blocks may only contain arrays.")

		# Test line, should either be a statement or a code block
		if isinstance(line[0], str):
			# we have a statement
			result = self.resolve_statement(line)

			if isinstance(result, RepeatStatement):
				# repeat line if script deems statement not fullfilled
				self.script = [line] + self.script
			elif isinstance(result, list) and len(result) > 0 and isinstance(result[0], list):
				# if we have another block, inject individual statements on script
				# usually this would be the case on IF statements returning the
				# next block to execute for example.
				self.script = result + self.script
			else:
				return result

		elif isinstance(line[0], list):
			# inject entire blocks into script to resolve inlined blocks
			self.script = line + self.script

	def resolve_statement(self, exp):
		"""Resolves a statement calling nested argument statements if any provided"""
		cmd = exp[0]
		fn = self.ctx.get(cmd, self.ctx.get(CMD_UNSUPPORTED))
		if fn == self.ctx.get(CMD_UNSUPPORTED):
			args = [cmd]
			cmd = CMD_UNSUPPORTED
		else:
			args = [ self.resolve_argument(arg) for arg in exp[1:] ]

		result = fn(self.ctx, *args)
		return result

	def resolve_argument(self, arg):
		"""Resolves argument values and calls functions"""
		# check if we have a statement
		if isinstance(arg, list):
			if arg[0] == CMD_ARRAY:
				# we have an array, resolve it to a list of items
				return arg[1:]
			elif isinstance(arg[0], list):
				# we have a block, return it as is
				return arg
			else:
				# we have a statement
				return self.resolve_statement(arg)
		else:
			# we have some other native type, return that
			return arg