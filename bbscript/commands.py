from functools import reduce
import re
from .errors import InvalidOperation
from .flags import StopExecutionNoRecover
from termcolor import colored
from .constants import \
	CMD_ARRAY, \
	CMD_VAR, \
	CMD_VAL, \
	CMD_IF, \
	CMD_INT, \
	CMD_FLOAT, \
	CMD_STRING, \
	CMD_BOOL, \
	CMD_IN, \
	CMD_SET, \
	CMD_UNDEFINED, \
	CMD_UNSUPPORTED, \
	CMD_LOG, \
	CMD_MATH, \
	CMD_CONDITION, \
	CMD_IS_EVEN, \
	CMD_IS_ODD, \
	CMD_DBUG
import pprint
DBUG_PP = pprint.PrettyPrinter(indent=2, depth=2)

def flt(val):
	try:
		return float(val)
	except:
		return 0

def cint(val):
	try:
		return int(val)
	except:
		return 0

def unsupported_function(ctx, cmd):
	print("UNSUPPORTED FUNCTION: ", cmd)
	ctx.update({
		"error": "Unsupported command: {}".format(cmd)
	})
	return StopExecutionNoRecover()

def cmd_math(ctx, op, left, right):
	type_fn = flt
	if isinstance(left, int):
		type_fn = cint
	if isinstance(right, int):
		type_fn = cint

	left = type_fn(left)
	right = type_fn(right)

	if op == "+":
		return left + right
	elif op == "-":
		return left - right
	elif op == "*":
		return left * right
	elif op == "/":
		return left / right
	elif op == "%":
		return left * (right / 100)
	elif op == "MOD":
		return left % right

	return InvalidOperation("op must be one of +, -, *, /, %, MOD")

def cmd_is_even(ctx, val):
	return flt(val) % 2 == 0

def cmd_is_odd(ctx, val):
	return flt(val) % 2 != 0

def cmd_condition(ctx, op, left, right):
	if op == "==":
		return left == right
	elif op == "!=":
		return left != right
	elif op == "~" or op == "!~":
		pattern = right.replace(r"[\s\.%]+", ".*?")
		result = re.match(pattern, left)
		if op == "~":
			return result != None
		elif op == "!~":
			return result == None
	elif op == ">":
		return left > right
	elif op == "<":
		return left < right
	elif op == ">=":
		return left >= right
	elif op == "<=":
		return left <= right
	elif op == "AND":
		return left and right
	elif op == "OR":
		return left or right
	elif op == "NOT":
		return not (left and right)
	elif op == "XOR":
		return bool(left) ^ bool(right)

	return InvalidOperation("op must be one of ==, !=, ~, ~=, <, >, <=, >=, AND, OR, NOT, XOR")

def cmd_dbug(ctx, id, cmd, label=None):
	print(colored("[{}] {}".format(id, label if label else " Debug:"), "yellow", attrs=['bold']))
	for line in cmd:
		print("  ", DBUG_PP.pformat(line))
	return cmd

COMMANDS = {
	CMD_DBUG: cmd_dbug,

	CMD_MATH: cmd_math,
	CMD_IS_EVEN: cmd_is_even,
	CMD_IS_ODD: cmd_is_odd,

	CMD_CONDITION: cmd_condition,

	CMD_UNDEFINED: lambda ctx: None,
	CMD_INT: lambda ctx, val: cint(val),
	CMD_FLOAT: lambda ctx, val: flt(val),
	CMD_STRING: lambda ctx, val: str(val),
	CMD_BOOL: lambda ctx, val: bool(val),
	CMD_IN: lambda ctx, a, b: a in b,
	
	CMD_ARRAY: lambda ctx, *args: list(args),
	CMD_VAR: lambda ctx, *args: ctx.get(args[0]),
	CMD_VAL: lambda ctx, *args: args[0],

	CMD_IF: lambda ctx, cond, true_block, false_block=None: true_block if cond else false_block or [],

	CMD_SET: lambda ctx, *args: ctx.update({args[0]: args[1]}),

	CMD_LOG: lambda ctx, *args: print(*args),

	CMD_UNSUPPORTED: lambda ctx, *args: unsupported_function(ctx, args[0])
}