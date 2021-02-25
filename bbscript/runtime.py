from .constants import \
	TYPE_BLOCK, \
	TYPE_BOOLEAN, \
	TYPE_EXPRESSION, \
	TYPE_LIST, \
	TYPE_NUMERIC, \
	TYPE_STRING, \
	CMD_UNSUPPORTED, \
	CMD_ARRAY, \
	STEP_BEFORE, \
	STEP_AFTER

from .commands import COMMANDS
import time

def prime_context(ctx):
	ctx.update(COMMANDS)
	ctx.update({
		"RUN": lambda script, ctx: run(script, ctx)
	})

def run(script, ctx):
	prime_context(ctx)
	run_block(script, ctx)

def run_block(block, ctx):
	for statement in block:
		resolve_expression(statement, ctx)

def resolve_expression(exp, ctx):
	exp_type = resolve_exp_type(exp)

	if exp_type == TYPE_EXPRESSION:
		cmd = exp[0]
		args = [ resolve_expression(arg, ctx) for arg in exp[1:] ]

		fn = ctx.get(cmd, ctx.get(CMD_UNSUPPORTED))
		if fn == ctx.get(CMD_UNSUPPORTED):
			args = [cmd]
			cmd = CMD_UNSUPPORTED

		result = fn(args, ctx)
		return result
	elif exp_type == TYPE_LIST:
		args = [ resolve_expression(arg, ctx) for arg in exp[1:] ]

		return args
	else:
		return exp

def resolve_exp_type(value):
	"""Resolves data types of passed values. Internally called to distinguish expressions from data.
	
	Params:
		value: * -> A value to test its type.

	Returns:
		The value type as understood by bloom brackets
	"""

	if type(value) == int or type(value) == float:
		return TYPE_NUMERIC
	elif type(value) == bool:
		return TYPE_BOOLEAN
	elif isinstance(value, str):
		return TYPE_STRING
	elif isinstance(value, list):
		if value[0] == CMD_ARRAY:
			return TYPE_LIST
		elif isinstance(value[0], list):
			return TYPE_BLOCK
		else:
			return TYPE_EXPRESSION

	return None