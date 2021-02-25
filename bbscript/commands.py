from functools import reduce
from .constants import \
	CMD_ARRAY, \
	CMD_VAR, \
	CMD_VAL, \
	CMD_IF, \
	CMD_EQUALS, \
	CMD_NOT_EQUALS, \
	CMD_LIKE, \
	CMD_NOT_LIKE, \
	CMD_GREATER_THAN, \
	CMD_LESS_THAN, \
	CMD_GREATER_AND_EQUAL, \
	CMD_BETWEEN, \
	CMD_LESS_AND_EQUAL, \
	CMD_ADD, \
	CMD_SUBTRACT, \
	CMD_MULTIPLY, \
	CMD_DIVIDE, \
	CMD_AND, \
	CMD_OR, \
	CMD_NOT, \
	CMD_XOR, \
	CMD_TRUE, \
	CMD_FALSE, \
	CMD_INT, \
	CMD_FLOAT, \
	CMD_STRING, \
	CMD_BOOL, \
	CMD_IN, \
	CMD_SET, \
	CMD_UNDEFINED, \
	CMD_UNSUPPORTED, \
	CMD_LOG

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

def unsupported_function(cmd, ctx):
	print("UNSUPPORTED FUNCTION: ", cmd)
	ctx.update({
		"error": "Unsupported command: {}".format(cmd)
	})


COMMANDS = {
	CMD_ADD: lambda args, ctx: sum(args),
	CMD_SUBTRACT: lambda args, ctx: reduce(lambda a, b: a - b, args),
	CMD_MULTIPLY: lambda args, ctx: reduce(lambda a, b: a * b, args),
	CMD_DIVIDE: lambda args, ctx: reduce(lambda a, b: a / b, args),

	CMD_TRUE: lambda args, ctx: reduce(lambda a, b: a == b, args),
	CMD_FALSE: lambda args, ctx: reduce(lambda a, b: a != b, args),
	CMD_EQUALS: lambda args, ctx: reduce(lambda a, b: a == b, args),
	CMD_NOT_EQUALS: lambda args, ctx: reduce(lambda a, b: a != b, args),

	CMD_LIKE: lambda args, ctx: args[0] in args[1],
	CMD_NOT_LIKE: lambda args, ctx: args[0] not in args[1],
	CMD_BETWEEN: lambda args, ctx: args[0] > args[1] and args[0] < args[2],

	CMD_GREATER_THAN: lambda args, ctx: reduce(lambda a, b: flt(a) > flt(b), args),
	CMD_GREATER_AND_EQUAL: lambda args, ctx: reduce(lambda a, b: flt(a) >= flt(b), args),
	CMD_LESS_THAN: lambda args, ctx: reduce(lambda a, b: flt(a) < flt(b), args),
	CMD_LESS_AND_EQUAL: lambda args, ctx: reduce(lambda a, b: flt(a) <= flt(b), args),

	CMD_AND: lambda args, ctx: all(args),
	CMD_OR: lambda args, ctx: any(args),
	CMD_XOR: lambda args, ctx: reduce(lambda a, b: bool(a) ^ bool(b), args),
	CMD_NOT: lambda args, ctx: not all(args),

	CMD_UNDEFINED: lambda args, ctx: None,
	CMD_INT: lambda args, ctx: cint(args[0]),
	CMD_FLOAT: lambda args, ctx: flt(args[0]),
	CMD_STRING: lambda args, ctx: str(args[0]),
	CMD_BOOL: lambda args, ctx: bool(args[0]),
	CMD_IN: lambda args, ctx: args[0] in args[1],
	
	CMD_ARRAY: lambda args, ctx: list(args),
	CMD_VAR: lambda args, ctx: ctx.get("VAR")(args),
	CMD_VAL: lambda args, ctx: args[0],

	CMD_IF: lambda args, ctx: ctx["RUN"](args[1], ctx) if args[0] else ctx["RUN"](args[2] if len(args) > 2 else [], ctx),

	CMD_SET: lambda args, ctx: ctx.update({args[0]: args[1]}),

	CMD_LOG: lambda args, ctx: print(*args),

	CMD_UNSUPPORTED: lambda args, ctx: unsupported_function(args[0], ctx)
}