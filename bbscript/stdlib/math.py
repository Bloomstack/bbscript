import math
from ..meta import bbmeta
from ..errors import InvalidOperation
from .utils import flt, cint

@bbmeta(
	description="Calculates a mathematical operation given the operator and two values.",
	inputs=[
		dict(name="op", type="str", options=["+", "-", "*", "/", "%", "MOD", "WRAP"]),
		dict(name="left", type=dict(union=["float", "int"],	match="right")),
		dict(name="right", type=dict(union=["float", "int"], match="left"))
	],
	outputs=dict(name="result", type=dict(union=["float", "int"], match=["left", "right"]))
)
def cmd_math(ctx, op: str, left, right):
	"""
			To perform math operations.

			Parameters:
			-----------
			op: Math operation to perform
			left: left value
			right: right value

			Returns:
			--------
			value of the left and right parameter with respect to the op.

	"""
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
		return math.fmod(left, right)
	elif op == "WRAP":
		return left % right

	raise InvalidOperation("op must be one of +, -, *, /, %, MOD")