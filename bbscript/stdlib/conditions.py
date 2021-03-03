import re
from typing import Union
from ..meta import bbmeta
from .utils import flt
from ..errors import InvalidOperation

@bbmeta(
	description="Given two values computes a true or false value depending on the operator selected.",
	inputs=[
		dict(
			name="op", 
			type="str",
			description="The condition operator.",
			options=[
				"==", "!=", "IN", "NOT IN", "~", "!~", ">", "<", ">=", "<=", "AND", "OR", "NOT", "XOR"
			]
		),
		dict(
			name="left",
			description="The left side of the condition",
			type=dict(
				union=["str", "int", "float", "bool"]
			)
		),
		dict(
			name="right",
			description="The right side of the condition",
			type=dict(
				union=["str", "int", "float", "bool"]
			)
		)
	],
	outputs=dict(name="result", type="bool"),
	errors=[
		dict(
			name="InvalidOperation",
			description="Raised when an invalid operator is provided."
		)
	]
)
def cmd_condition(ctx, op, left, right):
	if op == "==":
		return left == right
	elif op == "!=":
		return left != right
	elif op == "IN":
		return right in left
	elif op == "NOT IN":
		return right not in left
	elif op == "~" or op == "!~":
		left = str(left)
		right = str(right)
		pattern = ".*?{}.*?".format(re.sub(r"[\s\.%]+", ".*?", right.strip().lower()))
		result = re.match(pattern, left.lower())
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

	raise InvalidOperation("op must be one of ==, !=, ~, ~=, <, >, <=, >=, AND, OR, NOT, XOR")

@bbmeta(
	description="Branching logic. If condition is true the true_block branch will be executed, else the false_block",
	inputs=[
		dict(
			name="cond",
			type="bool"
		)
	],
	outputs=[
		dict(
			name="true_block",
			type="block"
		),
		dict(
			name="false_block",
			type="block"
		)
	]
)
def cmd_if(ctx, cond, true_block, false_block=None):
	return true_block if cond else false_block or []