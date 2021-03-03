from .utils import cmd_log, cmd_unsupported_function
from .math import cmd_math
from .even_odd import cmd_is_even, cmd_is_odd
from .conditions import cmd_condition, cmd_if
from .debug import cmd_dbug
from .convertions import cmd_bool, cmd_float, cmd_int, cmd_string, cmd_undefined
from .values import cmd_array, cmd_doc, cmd_set, cmd_var
from ..constants import \
	CMD_ARRAY, \
	CMD_VAR, \
	CMD_DOC, \
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

def load_stdlib(ctx):
	ctx.update({
		CMD_DBUG: cmd_dbug,

		CMD_MATH: cmd_math,
		CMD_IS_EVEN: cmd_is_even,
		CMD_IS_ODD: cmd_is_odd,

		CMD_CONDITION: cmd_condition,
		CMD_IF: cmd_if,

		CMD_INT: cmd_int,
		CMD_FLOAT: cmd_float,
		CMD_STRING: cmd_string,
		CMD_BOOL: cmd_bool,
		CMD_UNSUPPORTED: cmd_undefined,

		CMD_ARRAY: cmd_array,
		CMD_VAR: cmd_var,
		CMD_DOC: cmd_doc,

		CMD_SET: cmd_set,
		CMD_LOG: cmd_log,

		CMD_UNSUPPORTED: cmd_unsupported_function
	})